# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 6: Proyecto Integrador Blog
"""

from bs4 import BeautifulSoup

def cargar_blog():
    try:
        with open("../mock_pages/blog.html", "r", encoding="utf-8") as f:
            return BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        try:
            with open("mock_pages/blog.html", "r", encoding="utf-8") as f:
                return BeautifulSoup(f, "html.parser")
        except FileNotFoundError:
            print("Error: No se pudo encontrar 'blog.html'.")
            return None

def scraping_blog():
    sopa = cargar_blog()
    if sopa is None:
        return

    posts = []

    # 1. Extraer los artículos
    articulos = sopa.find_all('article', class_='post-card')

    for art in articulos:
        # ID
        art_id = art.get('id')
        
        # Título y Enlace
        title_a = art.find('h2', class_='post-title').find('a')
        titulo = title_a.text.strip()
        enlace = title_a.get('href')
        
        # Autor
        author_tag = art.find('span', class_='author')
        autor = author_tag.text.strip() if author_tag else "Anónimo"
        
        # Fecha
        time_tag = art.find('time', class_='date')
        fecha_texto = ""
        fecha_iso = ""
        if time_tag:
            fecha_texto = time_tag.text.strip()
            fecha_iso = time_tag.get('datetime', '')
            
        # Etiquetas (recorrer los enlaces que tengan clase 'tag' dentro del artículo)
        # Nota: evitamos coger etiquetas del sidebar buscando dentro de este artículo
        tags_tags = art.find_all('a', class_='tag')
        etiquetas = [tag.text.strip() for tag in tags_tags]
        
        # Guardar post
        post = {
            "id": art_id,
            "titulo": titulo,
            "enlace": enlace,
            "autor": autor,
            "fecha_texto": fecha_texto,
            "fecha_iso": fecha_iso,
            "etiquetas": etiquetas
        }
        posts.append(post)

    print(f"Total artículos extraídos: {len(posts)}\n")

    # 2. Análisis y Filtrado de Datos
    
    # A) Contar posts por autor
    autores_count = {}
    for p in posts:
        autor = p["autor"]
        autores_count[autor] = autores_count.get(autor, 0) + 1
        
    print("Artículos por autor:")
    for autor, cantidad in autores_count.items():
        print(f"  - {autor}: {cantidad}")

    # B) Buscar posts con la etiqueta 'Python'
    tag_buscada = 'Python'
    python_posts = [p for p in posts if tag_buscada in p["etiquetas"]]
    
    print(f"\nArtículos con etiqueta '{tag_buscada}':")
    for p in python_posts:
        print(f"  * {p['titulo']} (por {p['autor']})")


if __name__ == "__main__":
    scraping_blog()
