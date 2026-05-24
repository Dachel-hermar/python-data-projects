# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 2: Atributos y Selectores CSS
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
    tarjetas = sopa.find_all('div', class_='product-card')
    print(f"Se encontraron {len(tarjetas)} tarjetas de productos.")

    # 2. Recorre las tarjetas y extrae ID, título y enlace
    for tarjeta in tarjetas:
        card_id = tarjeta.get('id')  # o tarjeta['id']
        title_tag = tarjeta.find('h3', class_='product-title').find('a')
        titulo_texto = title_tag.text.strip()
        enlace = title_tag.get('href')  # o title_tag['href']
        print(f"ID: {card_id} | Producto: {titulo_texto} | Enlace: {enlace}")


def ejercicio_2_selectores_css():
    print("\n--- Parte 2: Selectores CSS (select y select_one) ---")
    sopa = cargar_ecommerce()
    if sopa is None:
        return

    # 1. Usa select_one para encontrar el primer encabezado h1 en la cabecera
    h1_select = sopa.select_one('header h1')
    print("H1 encontrado:", h1_select.text if h1_select else "No encontrado")

    # 2. Encuentra todas las imágenes que están dentro de las tarjetas de producto
    imagenes = sopa.select('.product-card img.product-image')
    print(f"Se encontraron {len(imagenes)} imágenes de producto.")
    for img in imagenes:
        print("Ruta imagen:", img.get('src'))

    # 3. Encuentra todos los enlaces de añadir al carrito
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
