# -*- coding: utf-8 -*-
"""
Solución al Ejercicio 3: Navegación por el Árbol DOM
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

def ejercicio_3_navegacion():
    sopa = cargar_blog()
    if sopa is None:
        return

    # 1. ENCONTRAR PADRES
    print("--- 1. Encontrar Elementos Padre ---")
    
    # Buscamos el primer span que tiene la clase 'author' y texto 'Carlos Gómez'
    author_span = sopa.find('span', class_='author')
    
    if author_span:
        # Navega al padre directo usando .parent
        padre_directo = author_span.parent
        print("Padre directo:", padre_directo.name)  # Debería ser 'span' (el del texto "Por Carlos Gómez")
        
        # Subimos hasta encontrar la etiqueta <article>
        articulo_contenedor = author_span.find_parent('article')
        print("Artículo contenedor (ID):", articulo_contenedor.get('id'))
        print("Título del artículo del autor:", articulo_contenedor.find('h2').text.strip())
    else:
        print("No se encontró el autor.")

    # 2. ACCEDER A HIJOS
    print("\n--- 2. Encontrar Elementos Hijos ---")
    sidebar = sopa.find('aside', class_='sidebar')
    if sidebar:
        # Recorremos los hijos filtrando solo etiquetas (ignorando strings vacíos)
        hijos_etiquetas = [hijo for hijo in sidebar.children if hijo.name is not None]
        print(f"La barra lateral tiene {len(hijos_etiquetas)} elementos hijos HTML.")
        for h in hijos_etiquetas:
            print(f"  * Hijo: <{h.name}> con texto: '{h.get_text().strip()}'")

    # 3. ACCEDER A HERMANOS (SIBLINGS)
    print("\n--- 3. Encontrar Elementos Hermanos ---")
    post_1 = sopa.find('article', id='post-1')
    if post_1:
        # Usamos .find_next_sibling('article') para encontrar el siguiente artículo
        post_2 = post_1.find_next_sibling('article')
        if post_2:
            titulo_post2 = post_2.find('h2').get_text().strip()
            print("Siguiente artículo encontrado (Hermano):", titulo_post2)
            print("ID del Hermano:", post_2.get('id'))


if __name__ == "__main__":
    ejercicio_3_navegacion()
