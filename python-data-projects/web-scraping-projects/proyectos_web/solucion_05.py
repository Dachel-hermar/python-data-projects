# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 5: Proyecto Integrador E-Commerce
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

    # 1. Encuentra todos los contenedores de producto
    tarjetas = sopa.find_all('div', class_='product-card')

    for tarjeta in tarjetas:
        # ID
        prod_id = tarjeta.get('id')
        
        # Marca
        brand_tag = tarjeta.find('span', class_='product-brand')
        marca = brand_tag.text.strip() if brand_tag else ""
        
        # Título y Enlace
        title_a = tarjeta.find('h3', class_='product-title').find('a')
        titulo = title_a.text.strip()
        enlace = title_a.get('href')
        
        # Calificación
        rating_container = tarjeta.find('div', class_='rating-container')
        puntuacion = None
        if rating_container:
            raw_score = rating_container.get('data-score')
            if raw_score:
                puntuacion = float(raw_score)
                
        # Opiniones
        review_count_tag = tarjeta.find('span', class_='review-count')
        opiniones = 0
        if review_count_tag:
            match = re.search(r'\d+', review_count_tag.text)
            if match:
                opiniones = int(match.group())
                
        # Precios
        price_tag = tarjeta.find('span', class_='price')
        precio = float(price_tag.text.replace("$", "").strip()) if price_tag else 0.0
        
        old_price_tag = tarjeta.find('span', class_='old-price')
        precio_original = None
        if old_price_tag:
            precio_original = float(old_price_tag.text.replace("$", "").strip())
            
        # Disponibilidad
        stock_tag = tarjeta.find('span', class_='stock-status')
        disponibilidad = stock_tag.text.strip() if stock_tag else "No especificado"
        
        # Construir producto
        producto = {
            "id": prod_id,
            "marca": marca,
            "titulo": titulo,
            "enlace": enlace,
            "puntuacion": puntuacion,
            "opiniones": opiniones,
            "precio": precio,
            "precio_original": precio_original,
            "disponibilidad": disponibilidad
        }
        productos.append(producto)

    print(f"Total productos extraídos: {len(productos)}")

    # 2. Exportar a JSON
    with open("productos.json", "w", encoding="utf-8") as jf:
        json.dump(productos, jf, indent=4, ensure_ascii=False)
    print("Catálogo exportado a productos.json")

    # 3. Exportar a CSV
    campos = ["id", "marca", "titulo", "enlace", "puntuacion", "opiniones", "precio", "precio_original", "disponibilidad"]
    with open("productos.csv", "w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=campos)
        writer.writeheader()
        writer.writerows(productos)
    print("Catálogo exportado a productos.csv")


if __name__ == "__main__":
    scraping_ecommerce()
