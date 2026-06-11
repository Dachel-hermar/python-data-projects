import requests
import pandas as pd
import matplotlib.pyplot as plt
import time
import os

def extraer_y_limpiar(simbolo, api_key):
    """Extrae datos de Alpha Vantage y los limpia. (Reutilizando la lógica que ya dominamos)"""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={simbolo}&apikey={api_key}"
    
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()
        
        # Validar si hubo un error de la API (ej. límite alcanzado o símbolo inválido)
        if "Time Series (Daily)" not in datos:
            print(f"[!] Error con {simbolo}. Es posible que necesites tu propia API Key.")
            return None
            
        # Convertir a DataFrame, limpiar y ordenar
        df = pd.DataFrame(datos['Time Series (Daily)']).T
        df = df.rename(columns={'4. close': simbolo})
        df = df[[simbolo]] # Nos quedamos solo con la columna de cierre
        df[simbolo] = pd.to_numeric(df[simbolo], errors='coerce')
        df.index = pd.to_datetime(df.index)
        df = df.sort_index() # <- ¡El truco que acabamos de repasar!
        
        return df

    except Exception as e:
        print(f"[!] Falló la conexión para {simbolo}: {e}")
        return None

def generar_reporte_lote(lista_empresas, api_key="demo"):
    print("=== INICIANDO PIPELINE DE GENERACIÓN DE REPORTES ===")
    
    dataframes = []
    
    # 1. EXTRACCIÓN EN LOTE (Bucle)
    for empresa in lista_empresas:
        print(f"-> Extrayendo datos de {empresa}...")
        df_limpio = extraer_y_limpiar(empresa, api_key)
        
        if df_limpio is not None:
            dataframes.append(df_limpio)
        
        # Esperar 2 segundos entre peticiones para respetar los límites de APIs gratuitas
        time.sleep(2)
        
    if not dataframes:
        print("No se pudo extraer ningún dato. Fin del programa.")
        return
        
    # 2. CONSOLIDACIÓN DE DATOS (pd.concat)
    print("\n=== CONSOLIDANDO Y CALCULANDO MÉTRICAS ===")
    df_final = pd.concat(dataframes, axis=1)
    df_final = df_final.ffill() # Llenar huecos vacíos
    
    # Nos enfocamos en los últimos 30 días para el reporte
    df_final = df_final.tail(30)
    
    # 3. CÁLCULO DE MÉTRICAS AGREGADAS
    print("Calculando Medias Móviles y Estadísticas Básicas...")
    
    # Creamos un segundo DataFrame solo para el reporte escrito
    reporte_stats = pd.DataFrame()
    reporte_stats['Precio Promedio'] = df_final.mean().round(2)
    reporte_stats['Precio Máximo'] = df_final.max()
    reporte_stats['Precio Mínimo'] = df_final.min()
    
    # Volatilidad (Diferencia entre el máximo y mínimo de los últimos 30 días)
    reporte_stats['Volatilidad (Max - Min)'] = (df_final.max() - df_final.min()).round(2)
    
    # 4. EXPORTACIÓN A CSV
    archivo_csv = "reporte_financiero_automatizado.csv"
    reporte_stats.to_csv(archivo_csv)
    print(f"\n[ÉXITO] Archivo CSV generado: {archivo_csv}")
    
    # 5. GENERACIÓN AUTOMÁTICA DE GRÁFICOS
    print("Generando gráficos del reporte...")
    plt.figure(figsize=(12, 6))
    
    # Graficamos todas las columnas (empresas) que haya en df_final
    for columna in df_final.columns:
        plt.plot(df_final.index, df_final[columna], marker='o', label=columna)
        
    plt.title("Reporte Automatizado: Últimos 30 días de Cotización", fontsize=14)
    plt.xlabel("Fecha")
    plt.ylabel("Precio de Cierre (USD)")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Para que las fechas no se amontonen en el eje X
    plt.xticks(rotation=45)
    plt.tight_layout() # Ajusta el diseño para que no se corten los elementos
    plt.show()
    archivo_png = "grafica_reporte_automatizado.png"
    plt.savefig(archivo_png)
    print(f"[ÉXITO] Gráfica guardada: {archivo_png}")
    print("\n=== PIPELINE TERMINADO CORRECTAMENTE ===")

if __name__ == "__main__":
    # NOTA: Para que funcione con varias empresas al mismo tiempo, 
    # DEBES cambiar la variable 'mi_llave' por tu propia API Key de Alpha Vantage.
    # La llave 'demo' solo dejará pasar a IBM e imprimirá un error controlado para AAPL y MSFT.
    
    mi_llave = "ECHOLOYMJKWHDA52" # Reemplaza "demo" con tu API Key real
    mis_empresas = ["IBM", "AAPL", "MSFT"]
    
    generar_reporte_lote(mis_empresas, mi_llave)
