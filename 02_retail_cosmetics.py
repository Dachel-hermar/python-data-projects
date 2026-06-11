
# 02_retail_cosmetics.py
import requests
import pandas as pd
import matplotlib.pyplot as plt

"""Proyecto: "Análisis de Productos Cosméticos
Objetivo: Usar Python para pedirle a la API de Makeup los datos actuales,
de productos de una marca específica (ejemplo: Maybelline).

Habilidades a desarrollar: Usar requests.get() con parámetros, 
entender cómo leer la respuesta en formato JSON, 
convertir esos datos crudos en un DataFrame de Pandas, 
limpiar los datos (convertir precios de texto a números), 
y crear una visualización básica del precio promedio por tipo de producto."
"""

def analizar_cosmeticos(marca="maybelline"):
    url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    
    # Parámetros para la API
    parametros = {
        "brand": marca
    }
    
    print(f"1. Buscando productos de la marca '{marca}'...\n")
    # Hacer la petición GET a la API con los parámetros
    respuesta = requests.get(url, params=parametros)
    
    if respuesta.status_code == 200:
        # Convertir la respuesta a formato JSON
        datos = respuesta.json()
        
        if not datos:
            print("No se encontraron resultados.")
            return

        print("2. ¡Datos descargados! Procesando...\n")
        
        # Crear DataFrame
        df = pd.DataFrame(datos)
        print("Columnas disponibles en el DataFrame:", df.columns, "\n")
        
        # Filtramos columnas útiles
        df = df[['id', 'name', 'product_type', 'price', 'rating']]
        print("Tipo de datos de las columnas del dataframe", df.dtypes)
        
        # RETO DE DATA SCIENCE (Limpieza de datos): 
        # Las APIs suelen devolver los números como texto (Strings).
        # Vamos a convertir la columna 'price' de texto a números flotantes (decimales).
        df['price'] = pd.to_numeric(df['price'], errors='coerce') # Esto convertirá los valores no numéricos a NaN (Not a Number)

        # Identificar los precios que no se pudieron convertir (que son NaN) para entender qué datos están causando problemas
        invalid_prices = df[
            pd.to_numeric(df['price'], errors='coerce').isna() & df['price'].notna()]['price'].unique()
        print(F"PRECIOS INVALIDOS: {invalid_prices}")
        
        # Quitamos los productos que no tienen precio para no afectar el análisis (solo si hay valores inválidos)
        if len(invalid_prices) > 0:
            df = df.dropna(subset=['price']) # Esto elimina las filas donde 'price' es NaN
        
        print(f"--- Top 5 Productos de {marca.capitalize()} ---") # Mostramos solo las primeras 5 filas para no saturar la salida
        print(df.head())
        print("\n")
        
        # Análisis Básico
        print(f"Precio Promedio: ${df['price'].mean():.2f}") # .2f formatea el número a 2 decimales
        print(f"Producto más caro cuesta: ${df['price'].max():.2f}") # .max() nos da el precio máximo
        print(f"Tipos de productos encontrados: {df['product_type'].unique()}\n") # .unique() nos muestra los tipos de productos sin repetir
        
        # Visualización de Datos
        # ¿Cuál es el precio promedio por TIPO de producto?
        precio_por_tipo = df.groupby('product_type')['price'].mean().sort_values() # Agrupamos por tipo de producto y calculamos el precio promedio, luego ordenamos
        
        # Crear una gráfica de barras para mostrar el precio promedio por tipo de producto
        plt.figure(figsize=(10, 6))
        # Crear un gráfico de barras horizontales
        precio_por_tipo.plot(kind='barh', color='coral', edgecolor='black')
        
        plt.title(f'Precio Promedio por Tipo de Producto ({marca.capitalize()})')
        plt.xlabel('Precio Promedio ($)')
        plt.ylabel('Tipo de Producto')
        plt.grid(axis='x', alpha=0.5) # Agrega una cuadrícula solo en el eje x para mejorar la legibilidad
        plt.tight_layout() # Ajusta el diseño para que no se corten los elementos
        
        print("Guardando la gráfica como 'precios_cosmeticos.png'...")
        plt.savefig("precios_cosmeticos.png")
        print("¡Gráfica guardada exitosamente!")
        
        plt.show() # Descomenta esto para ver la gráfica interactiva si lo corres en tu PC
        
    else:
        print(f"Error al conectar: {respuesta.status_code}")

if __name__ == "__main__":
    analizar_cosmeticos("maybelline")
