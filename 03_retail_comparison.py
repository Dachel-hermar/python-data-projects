# Comparativa de Marcas de Cosméticos: Maybelline vs Covergirl
# En este proyecto vamos a comparar dos marcas de cosméticos populares: Maybelline y Covergirl
# Usaremos la misma API de Makeup para obtener los datos de ambas marcas, y luego haremos un análisis competitivo.
# El objetivo es entender cuál de las dos marcas tiene un precio promedio más alto, y cómo se relaciona el precio con la calificación de los usuarios.
import requests
import pandas as pd
import matplotlib.pyplot as plt

def comparar_marcas(marcas):
    url = "http://makeup-api.herokuapp.com/api/v1/products.json"
    
    # Aquí guardaremos los datos de ambas marcas antes de unirlos
    lista_dataframes = []
    
    print("--- INICIANDO EXTRACCIÓN DE DATOS ---")
    for marca in marcas:
        print(f"Descargando catálogo de: {marca.upper()}...")
        parametros = {"brand": marca}
        respuesta = requests.get(url, params=parametros)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            df_temp = pd.DataFrame(datos)
            
            # Filtramos columnas y nos aseguramos de que sepamos de qué marca es cada fila
            df_temp = df_temp[['id', 'name', 'brand', 'price', 'rating']]
            lista_dataframes.append(df_temp)
        else:
            print(f"Error al descargar {marca}")
            
    # 1. Unir (Concatenar) los DataFrames en uno solo grande
    df_final = pd.concat(lista_dataframes, ignore_index=True) # ignore_index=True para resetear los índices después de concatenar
    print(f"Tipo de datos de las columnas del DataFrame final:\n{df_final.dtypes}\n") # Esto nos muestra el tipo de datos de cada columna para entender si necesitamos hacer limpieza de datos

    print("\n--- INICIANDO LIMPIEZA DE DATOS ---")
    # 2. Limpieza de precios (de texto a número flotante)
    # Esto convertirá los valores no numéricos a NaN (Not a Number)
    df_final['price'] = pd.to_numeric(df_final['price'], errors='coerce') 
    # Esto elimina las filas donde 'price' es NaN para no afectar el análisis
    df_final = df_final.dropna(subset=['price']) 
    print(f"Total de productos analizados: {len(df_final)}")
    
    # 3. Análisis Competitivo: ¿Quién es más caro en promedio?
    print("\n--- COMPARATIVA DE PRECIOS PROMEDIO ---")
    comparativa = df_final.groupby('brand')['price'].mean().round(2)
    print(comparativa)
    
    # 4. Visualización Avanzada (Scatter Plot: Precio vs Calificación)
    print("\nGenerando Gráfico de Dispersión (Scatter Plot)...")
    plt.figure(figsize=(10, 6))
    
    # Pintamos los puntos de cada marca con un color diferente
    colores = {'maybelline': 'blue', 'covergirl': 'purple'}
    
    for marca in marcas:
        # Filtramos los datos de una sola marca
        df_marca = new_func(marca, df_final) # Esto es para evitar repetir código, ya que vamos a hacer lo mismo para cada marca
        plt.scatter(
            df_marca['price'], 
            df_marca['rating'], 
            label=marca.capitalize(), 
            color=colores.get(marca, 'gray'),
            alpha=0.6, # Transparencia para ver si se superponen
            edgecolors='white',
            s=80 # Tamaño de los puntos
        )
        
    plt.title('Análisis Competitivo: Precio vs Calificación de Usuarios')
    plt.xlabel('Precio del Producto ($)')
    plt.ylabel('Calificación (0 a 5 Estrellas)')
    plt.legend(title="Marca")
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Guardamos la gráfica
    plt.savefig("precio_vs_calificacion.png")
    print("¡Gráfica guardada como 'precio_vs_calificacion.png'!")

        # Mostramos la gráfica
    plt.show()

# Función para filtrar el DataFrame por marca, para evitar repetir código
def new_func(marca, df_final):
    df_marca = df_final[df_final['brand'] == marca]
    return df_marca

if __name__ == "__main__":
    # Puedes agregar más marcas aquí si quieres experimentar: 'covergirl', 'clinique', 'dior'
    mis_marcas = ['maybelline', 'covergirl','clinique', 'dior']
    comparar_marcas(mis_marcas)
