# -*- coding: utf-8 -*-
"""
Ejercicio 5: Proyecto Integrador E-Commerce
--------------------------------------------
En este proyecto aplicarás todo lo aprendido para extraer un catálogo completo
de productos desde mock_pages/e_commerce.html.

Tu tarea:
1. Buscar todas las tarjetas de producto.
2. Extraer de cada una:
   - ID único (`id` del div).
   - Marca (`product-brand`).
   - Título del producto (`product-title`).
   - Enlace completo al producto (`href`).
   - Puntuación (extraída del atributo `data-score` en `rating-container`).
   - Cantidad de opiniones (número dentro del texto, ej: "(124 opiniones)").
   - Precio actual (convertido a float).
   - Precio original si existe (convertido a float, si no, None).
   - Disponibilidad (En stock, Pocas unidades, Agotado).
3. Exportar la lista de productos a un archivo JSON llamado 'productos.json'.
4. Exportar la lista de productos a un archivo CSV llamado 'productos.csv'.
"""

import json
import csv
import re
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

def scraping_ecommerce():
    sopa = cargar_ecommerce()
    if sopa is None:
        return

    productos = []

    # 1. Encuentra todos los contenedores de producto (.product-card)
    # TODO: tarjetas = ...
    tarjetas = sopa.find_all('div', class_='product-card')
    print(f"Se encontraron {len(tarjetas)} tarjeta de producto.")
    

    


    for tarjeta in tarjetas:
        # TODO: Extraer datos de la tarjeta de producto
        # - ID único (`id` del div).
        id_producto = tarjeta['id']
        # print(f"El id del producto es: {id_producto}")
        # - Marca (`product-brand`).
        marca_tag = tarjeta.find('span', class_="product-brand").text.strip()
        marca = marca_tag if marca_tag else "No especificada"
        # print(f"El nombre de la Marca es: {marca}")
        # - Título del producto (`product-title`).
        titulo = tarjeta.find('h3', class_="product-title").find('a')
        titulo_producto = titulo.text.strip()
        # print(f"El Título del producto: {titulo}")
        # - Enlace completo al producto (`href`).
        enlace = titulo.get("href")
        print(f"Los enlaces al producto es: {enlace}")
        
        # - Calificación (atributo 'data-score' del contenedor de calificación)
        rating_score = tarjeta.find('div', class_='rating-container').get('data-score')
        rating = float(rating_score) if rating_score else None
        # print(f"El número de Rating es: {rating}")
        
        # - Cantidad de opiniones: Extrae el número del texto '(124 opiniones)' usando expresiones regulares o reemplazos.
        texto = tarjeta.find('span', class_="review-count").get_text().strip()
        match_opiniones = re.search(r'\d+', texto)
        opiniones = int(match_opiniones.group()) if match_opiniones else 0
        # print(f"El número de Opiniones es: {Opiniones}")
        
        # - Precios: Limpia el símbolo '$' y convierte a float.
        # Pista: Ten cuidado, algunos productos no tienen precio original (old-price).
        precio = tarjeta.find("div", class_="price-container")
        clean_precio = precio.text.replace("$", "").replace(",", ".").strip().split()
        # print(precio)
        # print(clean_precio)
        
        for indice, pr in enumerate(clean_precio):
            """Este bucle es solo para verificar el contenido de clean_precio y 
            asegurarme de que se está limpiando correctamente el precio.
            Si clean_precio tiene más de un elemento, el primero será el precio actual y 
            el segundo será el precio original. Si solo tiene uno, ese será el precio actual y 
            el precio original será None."""
            # print(f"indice: {indice}, precio: {pr}")
        
            precio_actual = float(clean_precio[0])

        if len(clean_precio) > 1:
            precio_original = float(clean_precio[1])
        else:
            precio_original = None
                

     
        
        # - Disponibilidad: Extrae el texto de '.stock-status'.
        stock_tag = tarjeta.find('span', class_='stock-status')
        disponibilidad = stock_tag.text.strip() if stock_tag else "No especificado"
        
        # Construye el diccionario para cada producto
        producto = { 
                'id': id_producto,
                'Marca': marca,
                'Titulo': titulo_producto,
                'Enlace': enlace,
                'Rating': rating,
                'Opiniones': opiniones,
                'Precio': precio_actual,
                'Precio_original': precio_original,
                'Disponibilidad': disponibilidad
         }
        productos.append(producto)
        print(f"{producto}\n")

    print(f"Total productos extraídos: {len(productos)}")

    # 2. Exportar a JSON
    # TODO: Guarda la lista 'productos' en un archivo 'productos.json' con indentación de 4 espacios
    with open("productos.json", "w", encoding="utf-8") as jf:
        json.dump(productos, jf, indent=4, ensure_ascii=False)
    print("Catálogo exportado a productos.json")

    # 3. Exportar a CSV
    # TODO: Guarda la lista 'productos' en un archivo 'productos.csv'
    campos = ["id", "Marca", "Titulo", "Enlace", "Rating", "Opiniones", "Precio", "Precio_original", "Disponibilidad"]
    with open("productos.csv", "w", encoding="utf-8", newline="") as cf:
         writer = csv.DictWriter(cf, fieldnames=campos)
         writer.writeheader()
         writer.writerows(productos)
    print("Catálogo exportado a productos.csv")


if __name__ == "__main__":
    scraping_ecommerce()
