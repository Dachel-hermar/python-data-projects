# -*- coding: utf-8 -*-
"""
Ejercicio 1: Introducción a BeautifulSoup
-----------------------------------------
En este ejercicio aprenderás a cargar un documento HTML y a buscar
etiquetas básicas usando find() y find_all().
"""

from bs4 import BeautifulSoup

# HTML de ejemplo en formato string
html_doc = """
<html>
    <head>
        <title>Mi Primera Página Web</title>
    </head>
    <body>
        <h1>¡Bienvenido al Taller de Scraping!</h1>
        <p class="intro">Este es un párrafo de introducción sobre web scraping.</p>
        <p class="contenido">BeautifulSoup es una librería de Python increíble para parsear documentos HTML y XML.</p>
        <p class="contenido">Puedes encontrar más información en la documentación oficial.</p>
    </body>
</html>
"""

def ejercicio_1_basico_string():
    print("--- Parte 1: Parsear String HTML ---\n")
    
    # 1. Instancia el objeto BeautifulSoup con html_doc y el parser 'html.parser'
    sopa = BeautifulSoup(html_doc, "html.parser")
    
    if sopa is None:
        print("Sopa no inicializada.")
        return

    # 2. Imprime el título del HTML (accede directamente al atributo .title)
    titulo = sopa.title
    print(f"Título completo: {titulo}\n")
    print(f"Texto del título: {titulo.text}\n")

    # 3. Encuentra la etiqueta h1 e imprime su texto limpio usando .get_text()
    h1_tag = sopa.find("h1")
    print(f"H1 texto: {h1_tag.get_text()}\n")

    # 4. Encuentra el primer párrafo (etiqueta 'p') en el documento
    primer_p = sopa.find("p")
    print("Primer párrafo:", primer_p.text)


def ejercicio_1_ficheros_y_listas():
    print("\n--- Parte 2: Cargar Archivo Local e interactuar con Listas ---")
    
    # En esta parte, cargaremos una página de prueba local desde mock_pages/books_table.html
    path_html = "../mock_pages/books_table.html" # Ruta relativa correcta
    
    # 1. Abre el archivo en modo lectura con la codificación utf-8 correcta
    html_file= "../mock_pages/books_table.html"
    try:
        with open( html_file, "r", encoding="utf-8") as f:
            sopa = BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        # Para que funcione desde el directorio raíz o el directorio ejercicios
        try:
            with open("mock_pages/books_table.html", "r", encoding="utf-8") as f:
                sopa = BeautifulSoup(f, "html.parser")
        except FileNotFoundError:
            print("Error: No se pudo encontrar 'books_table.html'. Ejecuta el script desde la carpeta correcta.")
            return

    if sopa is None:
        print("Sopa no inicializada para el archivo local.")
        return

    # 2. Imprime el título de la página (<title>)
    print("Título de la página:", sopa.find("title"))

    # 3. Encuentra TODOS los elementos con la etiqueta 'th' (encabezados de tabla)
    ths = sopa.find_all("th")
    print(f"Se encontraron {len(ths)} columnas en la tabla.")
    # Imprime el texto de cada una de ellas
    for th in ths:
        print(th.get_text())

    # 4. Encuentra todos los elementos 'tr' (filas de la tabla) dentro del cuerpo de la tabla (tbody)
    # Pista: Puedes anidar búsquedas. Primero encuentra la etiqueta 'tbody' y luego busca 'tr' dentro de ella.
    body_tabla = sopa.find("tbody")
    filas = sopa.find_all("tr")
    print(f"La tabla contiene {len(filas)} filas de datos.")
    for indice,fila in enumerate(filas):
        columnas= fila.find_all("td")
        

        # Imprimimos los datos básicos de cada fila
        # Las columnas son: ID, Título, Autor, Año, Género, Puntuación, Precio
        if len(columnas) >= 3:
            book_id = columnas[0].text.strip()
            titulo = columnas[1].text.strip()
            autor = columnas[2].text.strip()
            print(f"  * [{book_id}] {titulo} - {autor}")
    


if __name__ == "__main__":
    ejercicio_1_basico_string()
    ejercicio_1_ficheros_y_listas()
