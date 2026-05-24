# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 1: Introducción a BeautifulSoup
"""

from bs4 import BeautifulSoup

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
    print("--- Parte 1: Parsear String HTML ---")
    
    # 1. Instancia el objeto BeautifulSoup
    sopa = BeautifulSoup(html_doc, 'html.parser')
    
    # 2. Imprime el título del HTML
    titulo = sopa.title
    print("Título completo:", titulo)
    print("Texto del título:", titulo.text)

    # 3. Encuentra la etiqueta h1 e imprime su texto limpio
    h1_tag = sopa.find('h1')
    print("H1 texto:", h1_tag.get_text())

    # 4. Encuentra el primer párrafo (etiqueta 'p')
    primer_p = sopa.find('p')
    print("Primer párrafo:", primer_p.text)


def ejercicio_1_ficheros_y_listas():
    print("\n--- Parte 2: Cargar Archivo Local e interactuar con Listas ---")
    
    # En esta parte, cargaremos una página de prueba local desde mock_pages/books_table.html
    try:
        with open("../mock_pages/books_table.html", "r", encoding="utf-8") as f:
            sopa = BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        try:
            with open("mock_pages/books_table.html", "r", encoding="utf-8") as f:
                sopa = BeautifulSoup(f, "html.parser")
        except FileNotFoundError:
            print("Error: No se pudo encontrar 'books_table.html'.")
            return

    # 2. Imprime el título de la página
    print("Título de la página:", sopa.title.text)

    # 3. Encuentra todos los elementos 'th'
    ths = sopa.find_all('th')
    print(f"Se encontraron {len(ths)} columnas en la tabla.")
    for th in ths:
        print(f"- {th.get_text().strip()}")

    # 4. Encuentra todos los elementos 'tr' dentro del body de la tabla
    body_tabla = sopa.find('tbody')
    filas = body_tabla.find_all('tr')
    print(f"La tabla contiene {len(filas)} filas de datos.")
    for fila in filas:
        columnas = fila.find_all('td')
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
