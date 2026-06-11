# Análisis de Acciones con Alpha Vantage
"""En este proyecto vamos a usar la API de Alpha Vantage para obtener datos históricos de precios de acciones. 
El objetivo es aprender a manejar APIs financieras, limpiar datos de series de tiempo, 
y crear una visualización básica del precio de cierre a lo largo del tiempo."""

import requests
import pandas as pd
import matplotlib.pyplot as plt

def analizar_acciones_av():
    # 1. El Endpoint principal de Alpha Vantage
    url = "https://www.alphavantage.co/query"
    
    # 2. Los Parámetros (Aquí incluimos la "Llave" o API Key)
    # Nota: Alpha Vantage nos presta la llave "demo" para hacer pruebas, pero 
    # solo funciona para la acción de "IBM". Para otras empresas (AAPL, MSFT) 
    # necesitarás crear tu propia llave gratuita en su página web.
    parametros = {
        "function": "TIME_SERIES_DAILY", # Queremos precios diarios
        "symbol": "AAPL",                 # Empresa a analizar
        "apikey": "ECHOLOYMJKWHDA52"     # Nuestra llave de acceso
    }
    
    print(f"Conectando a Wall Street para descargar datos de {parametros['symbol']}...")
    respuesta = requests.get(url, params=parametros)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print(f"¡Datos obtenidos! Estructurando la tabla...\n{datos.keys()}\n") # Esto nos muestra las llaves principales del JSON para entender su estructura
        # Alpha Vantage puede devolver un mensaje de error o límite dentro del JSON
        if "Information" in datos:
            print("Límite de la API alcanzado. Intenta de nuevo en un minuto.")
            return
            
        print("¡Datos obtenidos! Estructurando la tabla...\n")
        
        # 3. Navegar el JSON de Finanzas
        # Alpha Vantage guarda los precios dentro de la llave "Time Series (Daily)"
        series_diarias = datos['Time Series (Daily)']
        print(f"Ejemplo de una entrada de la serie temporal:\n{list(series_diarias.items())[0]}\n") # Esto nos muestra un ejemplo de cómo vienen los datos para entender qué columnas tenemos y qué formato tienen
        
        # 4. Crear el DataFrame
        # Al convertir este diccionario, Pandas pone las fechas como columnas.
        # Usamos .T (Transponer) para que las fechas sean las filas (Índice).
        df = pd.DataFrame(series_diarias)
        print(f"Columnas originales que envía la API:\n{df.columns}\n") # Esto nos muestra las columnas originales para entender qué datos tenemos antes de limpiarlos
        df = pd.DataFrame(series_diarias).T
        print(f"Columnas originales que envía la API para {parametros['symbol']}:\n{list(df.columns)}\n") # Esto nos muestra las columnas originales en la terminal para entender qué datos tenemos antes de limpiarlos
        print(df.head().dtypes) # Esto nos muestra las últimas filas del DataFrame para entender cómo vienen los datos antes de limpiarlos
        # Renombramos las columnas para que sean más limpias
        df = df.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        })
        
        # 5. RETO DATA SCIENCE: Limpieza de Series de Tiempo (Time Series)
        # Convertimos el Índice (las fechas) al formato datetime real de Pandas
        df.index = pd.to_datetime(df.index)
        
        # Convertimos todas las columnas (que vienen como texto) a números decimales flotantes
        df = df.astype(float)
        
        # Ordenamos del más antiguo al más reciente
        df = df.sort_index()
        
        print("--- Últimos 5 días de cotización ---")
        print(df[['Open', 'Close']].tail())
        print("\n")
        
        # 6. Visualización Financiera Básica
        plt.figure(figsize=(12, 6))
        # Graficamos el precio de Cierre (Close)
        plt.plot(df.index, df['Close'], color='green', linewidth=2, label="Precio de Cierre")
        
        plt.title(f"Histórico de Precios de {parametros['symbol']} (Últimos 100 Días)")
        plt.xlabel("Fecha")
        plt.ylabel("Precio en USD ($)")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend() # Agrega una leyenda para identificar la línea del gráfico
        
        plt.savefig("grafico_financiero.png")
        print("¡Gráfica histórica guardada como 'grafico_financiero.png'!")
        # Mostramos la gráfica
        plt.show()
        
    else:
        print(f"Error de conexión: {respuesta.status_code}")

if __name__ == "__main__":
    analizar_acciones_av()
