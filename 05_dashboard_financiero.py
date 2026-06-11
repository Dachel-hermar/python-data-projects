import streamlit as st
import requests
import pandas as pd
import time


"""Proyecto: Dashboard Financiero Interactivo"""
"""Objetivo: Crear un dashboard que permita a los usuarios comparar el rendimiento histórico de varias empresas a través de gráficos interactivos.
Habilidades a desarrollar: Python, Pandas, Matplotlib, Streamlit, manejo de APIs, limpieza de datos, diseño de interfaces, escalabilidad y buenas prácticas de programación (DRY Principle).
"""

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Dashboard Financiero", layout="wide") # layout="wide" para usar todo el ancho de la página   
st.title("📈 Dashboard Financiero Interactivo")
st.markdown("Analiza múltiples empresas y compara su rendimiento histórico.")

# --- 1. FUNCIÓN MODULAR DE EXTRACCIÓN Y LIMPIEZA (DRY Principle) ---
# Separamos la lógica de conexión y limpieza de la interfaz visual.
def obtener_datos_empresa(simbolo, api_key):
    """
    Se conecta a la API, descarga los datos, los limpia y maneja errores.
    """
    url = "https://www.alphavantage.co/query"
    parametros = {
        "function": "TIME_SERIES_DAILY",
        "symbol": simbolo.strip().upper(), # Limpieza básica del texto (quitar espacios)
        "apikey": api_key
    }
    
    try:
        # Petición a la API
        respuesta = requests.get(url, params=parametros)
        
        # Validar conexión HTTP
        if respuesta.status_code != 200:
            return None, f"Error HTTP {respuesta.status_code}"
            
        datos = respuesta.json()
        
        # Manejo de Errores Específicos de la API
        if "Information" in datos or "Note" in datos:
            return None, "Límite de la API alcanzado. Espera un momento."
        if "Error Message" in datos:
            return None, f"Símbolo inválido: {simbolo}"
            
        # Extracción del JSON Anidado
        series = datos.get('Time Series (Daily)', {})
        """Si la serie temporal está vacía, es probable que el símbolo sea incorrecto o que la API no tenga datos para esa empresa.
        En ese caso, devolvemos un mensaje de error específico para que el usuario sepa qué pasó."""
        if not series:
            return None, "No se encontraron datos de la serie temporal."
            
        # Convertir a DataFrame
        df = pd.DataFrame(series).T
        
        # Para inspección: Mostrar las columnas originales en la terminal
        print(f"\n[INFO] Columnas originales que envía la API para {simbolo}:")
        print(list(df.columns))
        
        # --- PROCESO RIGUROSO DE LIMPIEZA DE DATOS ---
        df = df.rename(columns={'4. close': 'Precio_Cierre'})
        # Convertir precios a números, si hay un texto raro, lo vuelve nulo (NaN)
        df['Precio_Cierre'] = pd.to_numeric(df['Precio_Cierre'], errors='coerce')
        # Limpiar filas con precios nulos
        df = df.dropna(subset=['Precio_Cierre'])
        # Convertir el índice a formato fecha
        df.index = pd.to_datetime(df.index)
        # Ordenar cronológicamente
        df = df.sort_index()
        
        # Devolvemos solo la columna de cierre, renombrada con el nombre de la empresa
        return df[['Precio_Cierre']].rename(columns={'Precio_Cierre': simbolo}), None

    except Exception as e:
        # Evita que todo el programa se caiga si hay un error crítico
        return None, f"Error inesperado: {str(e)}" # Esto es para capturar cualquier error que no hayamos anticipado, como problemas de conexión, errores de formato, etc.

# --- 2. INTERFAZ DE USUARIO (SIDEBAR) ---
st.sidebar.header("Parámetros de Análisis")
api_key_input = st.sidebar.text_input("API Key de Alpha Vantage", value="demo", type="password") # type="password" para ocultar el texto, aunque 'demo' es solo para pruebas
st.sidebar.markdown("*Nota: La llave 'demo' solo funciona con IBM.*")

# Recibimos un texto con varias empresas separadas por coma
empresas_input = st.sidebar.text_input("Empresas a comparar (separadas por coma)", value="IBM")

boton_analizar = st.sidebar.button("Analizar Datos")

# --- 3. LÓGICA PRINCIPAL (BUCLES Y ESCALABILIDAD) ---
if boton_analizar:
    # Convertimos el texto "AAPL, MSFT" en una lista real ['AAPL', 'MSFT']
    lista_empresas = [empresa.strip() for empresa in empresas_input.split(',')]
    
    st.info(f"Procesando {len(lista_empresas)} empresa(s)...")
    
    # Aquí almacenaremos los DataFrames limpios de cada empresa
    dataframes_limpios = []
    
    # BUCLE FOR (Escalabilidad: Funciona igual para 1 que para 100 empresas)
    barra_progreso = st.progress(0) # Barra de progreso para mejorar la experiencia del usuario
    
    for i, empresa in enumerate(lista_empresas):
        # Actualizamos la interfaz
        st.write(f"🔄 Extrayendo datos de: **{empresa}**...")
        
        # Usamos nuestra función modular
        df_empresa, error = obtener_datos_empresa(empresa, api_key_input) # Esto nos devuelve el DataFrame limpio o un mensaje de error
        
        if error:
            st.error(f"Error con {empresa}: {error}")
        else:
            dataframes_limpios.append(df_empresa)
            st.success(f"Datos de {empresa} procesados correctamente.")
            
        # Simulamos un pequeño retraso para no saturar APIs gratuitas
        time.sleep(0.5)  # Esto es solo para mejorar la experiencia visual, no es necesario en producción.
        barra_progreso.progress((i + 1) / len(lista_empresas)) # Actualizamos la barra de progreso
        
    # --- 4. CONSOLIDACIÓN DE DATOS Y GRÁFICAS ---
    if len(dataframes_limpios) > 0: # Solo intentamos graficar si tenemos al menos un DataFrame limpio
        st.subheader("📊 Comparativa de Rendimiento")
        
        # pd.concat es la forma profesional de unir datos.
        # Al unir por el eje de las columnas (axis=1), las fechas se alinean solas.
        df_consolidado = pd.concat(dataframes_limpios, axis=1)
        
        # Rellenar datos faltantes (forward fill) por si los días feriados no coinciden
        df_consolidado = df_consolidado.ffill()
        
        # Mostrar el gráfico interactivo nativo de Streamlit
        st.line_chart(df_consolidado)
        
        # Mostrar la tabla de datos limpios
        with st.expander("Ver tabla de datos limpios"):
            st.dataframe(df_consolidado.tail(10)) # Mostramos los últimos 10 días
    else:
        st.warning("No se pudo obtener datos válidos para ninguna empresa.")
