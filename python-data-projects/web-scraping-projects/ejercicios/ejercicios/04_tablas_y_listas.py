# -*- coding: utf-8 -*-
"""
Ejercicio 4: Extracción de Tablas y Listas
-------------------------------------------
En este ejercicio aprenderás a recorrer y parsear tablas HTML de forma
eficiente, estructurando los datos en objetos de Python (diccionarios y listas)
y limpiando textos (eliminar símbolos de moneda, convertir números, etc.).
"""

from bs4 import BeautifulSoup

def cargar_tabla_libros():
    try:
        with open("../mock_pages/books_table.html", "r", encoding="utf-8") as f:
            return BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        try:
            with open("mock_pages/books_table.html", "r", encoding="utf-8") as f:
                return BeautifulSoup(f, "html.parser")
        except FileNotFoundError:
            print("Error: No se pudo encontrar 'books_table.html'.")
            return None

def ejercicio_4_tablas():
    sopa = cargar_tabla_libros()
    if sopa is None:
        return

    # En este ejercicio queremos extraer todos los libros de la tabla y convertirlos
    # en una lista de diccionarios con claves limpias:
    # [
    #   {
    #       "id": "BK-01",
    #       "titulo": "Don Quijote de la Mancha",
    #       "autor": "Miguel de Cervantes",
    #       "anio": 1605,
    #       "genero": "Novela",
    #       "puntuacion": 4.9,
    #       "precio": 15.99
    #   },
    #   ...
    # ]

    lista_libros = []

    # 1. Localiza la tabla por su ID 'books-table'
    tabla = sopa.find('table', id='books-table')

    if tabla is None:
        print("Tabla no encontrada.")
        return

    # 2. Encuentra todas las filas (tr) que se encuentran dentro del cuerpo de la tabla (tbody)
    tbody = tabla.find('tbody')
    if tbody is None:
        print("No se encontró el cuerpo de la tabla.")
        return

    filas = tbody.find_all('tr')

    for fila in filas:
        # 3. Para cada fila, encuentra todas sus celdas (td)
        celdas = fila.find_all('td')

        if len(celdas) == 7:
            # 4. Extrae los valores de cada celda por su índice:
            # Índice 0: ID
            # Índice 1: Título
            # Índice 2: Autor
            # Índice 3: Año
            # Índice 4: Género
            # Índice 5: Puntuación
            # Índice 6: Precio
            book_id = celdas[0].text.strip()
            titulo = celdas[1].text.strip()
            autor = celdas[2].text.strip()
            anio = int(celdas[3].text.strip())
            genero = celdas[4].text.strip()
            puntuacion = float(celdas[5].text.strip())
            precio = float(celdas[6].text.replace("€", "").replace(",", ".").strip())

            # 5. Crea el diccionario para el libro y añádelo a 'lista_libros'
            libro = {
                "id": book_id,
                "titulo": titulo,
                "autor": autor,
                "anio": anio,
                "genero": genero,
                "puntuacion": puntuacion,
                "precio": precio
            }
            lista_libros.append(libro)

    # Imprime la lista de libros estructurada
    print(f"Se extrajeron {len(lista_libros)} libros correctamente:")
    for l in lista_libros:
        print(l)


if __name__ == "__main__":
    ejercicio_4_tablas()
