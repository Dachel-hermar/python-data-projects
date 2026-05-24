# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 4: Extracción de Tablas y Listas
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

    lista_libros = []

    # 1. Localiza la tabla por su ID 'books-table'
    tabla = sopa.find('table', id='books-table')
    
    if not tabla:
        print("Tabla no encontrada.")
        return

    # 2. Encuentra todas las filas (tr) dentro de tbody
    tbody = tabla.find('tbody')
    filas = tbody.find_all('tr')

    for fila in filas:
        # 3. Encuentra las celdas (td)
        celdas = fila.find_all('td')
        
        if len(celdas) == 7:
            # 4. Extraer y limpiar
            book_id = celdas[0].text.strip()
            titulo = celdas[1].text.strip()
            autor = celdas[2].text.strip()
            
            # Convertir el año a entero
            try:
                anio = int(celdas[3].text.strip())
            except ValueError:
                anio = None
                
            genero = celdas[4].text.strip()
            
            # Convertir puntuación a float
            try:
                puntuacion = float(celdas[5].text.strip())
            except ValueError:
                puntuacion = None
                
            # Limpiar precio (quitar €, espacios) y convertir a float
            raw_precio = celdas[6].text
            clean_precio = raw_precio.replace("€", "").replace(",", ".").strip()
            try:
                precio = float(clean_precio)
            except ValueError:
                precio = None
            
            # 5. Agregar a la lista
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

    # Imprimir resultado
    print(f"Se extrajeron {len(lista_libros)} libros correctamente:")
    for l in lista_libros:
        print(l)


if __name__ == "__main__":
    ejercicio_4_tablas()
