# Importar las librerías necesarias para hacer la petición a la API y manejar los datos
import requests # Para hacer la petición HTTP a la API
import pandas as pd # Para manejar los datos en formato de DataFrame, que es más fácil de analizar

"""OBjetivos del proyecto/ ejercicio:
1. Conectar a una API pública (FakeStore) para obtener datos de productos.
2. Convertir esos datos en un formato que podamos analizar (DataFrame de Pandas).
3. Realizar un análisis básico: Mostrar los primeros productos y calcular el precio promedio por categoría
"""
def analizar_tienda():
    # 1. Definir la URL de la API (Endpoint)
    url = "https://fakestoreapi.com/products"
    
    print("1. Conectando a la API de FakeStore...")
    # 2. Hacer la petición GET a la API
    respuesta = requests.get(url)
    
    # 3. Verificar que la petición fue exitosa (Código 200)
    if respuesta.status_code == 200:
        print("¡Conexión exitosa! Descargando datos...\n")
        
        # 4. Convertir la respuesta a formato JSON (que en Python se lee como listas y diccionarios)
        datos = respuesta.json()
        
        # 5. Convertir los datos crudos en un DataFrame de Pandas para su análisis
        df = pd.DataFrame(datos)
        print("Datos convertidos a DataFrame. Aquí tienes un vistazo de los datos:\n", df.columns, "\n")
        print(df.dtypes) # Esto nos muestra el tipo de datos de cada columna, para entender si necesitamos hacer limpieza de datos
        # Mostrar las primeras columnas para entender los datos
        print("--- Primeros 3 productos en la tienda ---")
        # Seleccionamos solo algunas columnas para que sea más fácil de leer
        print(df[['id', 'title', 'price', 'category']].head(3))
        
        print("\n")
        
        # 6. Pequeño ejercicio de Data Science: ¿Cuál es el precio promedio por categoría?
        print("--- Precio Promedio por Categoría ---")
        precio_promedio = df.groupby('category')['price'].mean().round(2) # Agrupamos por categoría, calculamos el promedio y redondeamos a 2 decimales
        print(precio_promedio)
        
    else:
        print(f"Error al conectar con la API. Código de estado: {respuesta.status_code}")

        # 7. ¿Cuál es el producto más caro de toda la tienda? 
    print("\n--- Producto más caro de la tienda ---")
    producto_mas_caro = df.loc[df['price'].idxmax()] # idxmax() nos da el índice del producto con el precio máximo
    print(f"Producto: {producto_mas_caro['title']}, Precio: ${producto_mas_caro['price']}")

if __name__ == "__main__":
    analizar_tienda()
