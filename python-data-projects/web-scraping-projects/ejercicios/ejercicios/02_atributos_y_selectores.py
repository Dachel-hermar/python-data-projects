# -*- coding: utf-8 -*-
"""
Ejercicio 2: Atributos y Selectores CSS
---------------------------------------
En este ejercicio aprenderás a filtrar por clase, extraer atributos
de etiquetas (como enlaces href e imágenes src) y usar selectores CSS.
"""

from bs4 import BeautifulSoup

def cargar_ecommerce():
    try:
        with open("../mock_pages/e_commerce.html", "r", encoding="utf-8") as f:
            return BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        try:
            with open("mock_pages/e_commerce.html", "r", encoding="utf-8") as f:
                return BeautifulSoup(f, "html.parser")
        except FileNotFoundError:
            print("Error: No se pudo encontrar 'e_commerce.html'.")
            return None

def ejercicio_2_atributos():
    print("--- Parte 1: Extraer Atributos y Filtrar por Clase ---")
    sopa = cargar_ecommerce()
    if sopa is None:
        return

    # 1. Encuentra todos los elementos div con clase 'product-card' usando find_all
    # Pista: recuerda usar el parámetro 'class_' en lugar de 'class'
    tarjetas = sopa.find_all('div', class_='product-card')
    print(f"Se encontraron {len(tarjetas)} tarjetas de productos.")

    # 2. Recorre las tarjetas y para cada una extrae:
    #   - El ID de la tarjeta (atributo 'id' del elemento div)
    #   - El título del producto (el enlace dentro de la clase 'product-title')
    #   - La dirección de enlace del producto (atributo 'href' de la etiqueta 'a' del título)
    # Pista: Para extraer atributos puedes usar corchetes ['id'] o el método .get('id')
    # TODO:
    for tarjeta in tarjetas:
        card_id = tarjeta['id']
        title_tag = tarjeta.find("h3", class_='product-title').find("a")
        titulo_texto = title_tag.text.strip()
        enlace = title_tag.get("href")
        print(f"ID: {card_id} | Producto: {titulo_texto} | Enlace: {enlace}")


def ejercicio_2_selectores_css():
    print("\n--- Parte 2: Selectores CSS (select y select_one) ---")
    sopa = cargar_ecommerce()
    if sopa is None:
        return

    # Los selectores CSS son muy potentes. Puedes usar:
    # .class para clases, #id para ids, espacio para descendientes, > para hijos directos.
    # select() devuelve una lista de coincidencias.
    # select_one() devuelve la primera coincidencia (equivalente a find).

    # 1. Usa select_one para encontrar el primer encabezado h1 en la cabecera
    # Selector sugerido: 'header h1'
    h1_select = sopa.select_one("h1")
    print("H1 encontrado:", h1_select.text if h1_select else "No encontrado")

    # 2. Encuentra todas las imágenes que están dentro de las tarjetas de producto
    # Selector sugerido: '.product-card img.product-image' o simplemente '.product-card img'
    # TODO: imagenes = ...
    imagenes = sopa.select('.product-card img')
    print(f"Se encontraron {len(imagenes)} imágenes de producto.")
    # Imprime la ruta de la imagen (atributo 'src') para cada una
    # TODO:
    for img in imagenes:
        print("Ruta imagen:", img.get('src'))

    # 3. Encuentra todos los enlaces de añadir al carrito
    # Selector sugerido: '.btn-add'
    btns = sopa.select('.btn-add')
    print(f"Encontrados {len(btns)} botones de añadir al carrito.")
    for btn in btns:
        # Algunos son enlaces (a), otros pueden ser botones (button)
        tipo_tag = btn.name
        texto = btn.text.strip()
        print(f"  * Botón [{tipo_tag}]: {texto}")


if __name__ == "__main__":
    ejercicio_2_atributos()
    ejercicio_2_selectores_css()
