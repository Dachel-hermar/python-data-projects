# -*- coding: utf-8 -*-
"""
Ejercicio 3: Navegación por el Árbol DOM
---------------------------------------
En este ejercicio aprenderás a navegar entre elementos padres,
hijos y hermanos utilizando BeautifulSoup.
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

    # 1. ENCONTRAR PADRES:
    # A veces encuentras un texto o etiqueta pequeña y necesitas el contenedor completo.
    # Encuentra la etiqueta con el nombre del autor 'Carlos Gómez'.
    # Luego, usa .parent para subir en la jerarquía hasta encontrar el bloque del artículo (post-card).
    # Pista: Puedes usar .parent repetidamente o buscar hacia arriba con .find_parent()
    print("--- 1. Encontrar Elementos Padre ---")
    
    # Busquemos el primer span que tiene la clase 'author' y texto 'Carlos Gómez'
    author_span = sopa.find('span', class_='author', string='Carlos Gómez')
    
    if author_span:
        # TODO: Navega al padre directo usando .parent
        padre_directo = author_span.parent
        print("Padre directo:", padre_directo.name)
        
        # TODO: Navega hacia arriba hasta encontrar la etiqueta <article> que contiene a Carlos Gómez
        # Pista: Puedes ir subiendo con .parent hasta que el name sea 'article'
        # o usar author_span.find_parent('article')
        articulo_contenedor = author_span.find_parent('article')
        print("Artículo contenedor (ID):", articulo_contenedor.get('id'))
        print("Título del artículo del autor:", articulo_contenedor.find('h2').text.strip())
    
    else:
        print("No se encontró el autor.")

    # 2. ACCEDER A HIJOS:
    # Encuentra la barra lateral (aside con clase 'sidebar') y recorre sus elementos hijos directos.
    print("\n--- 2. Encontrar Elementos Hijos ---")
    sidebar = sopa.find('aside', class_='sidebar')
    if sidebar:
        # Pista: sidebar.children devuelve un iterador de los hijos directos.
        # Ten en cuenta que en HTML, los saltos de línea e ingles de espacio en blanco se tratan como hijos de texto (NavigableString).
        # Para filtrar sólo etiquetas reales, puedes comprobar si el tipo tiene el atributo .name
        # TODO: Recorre los hijos e imprime solo aquellos que sean etiquetas HTML reales
        hijos_etiquetas = [hijo for hijo in sidebar.children if hijo.name is not None]
        print(f"La barra lateral tiene {len(hijos_etiquetas)} elementos hijos HTML.")
        for h in hijos_etiquetas:
             print(f"  * Hijo: <{h.name}> con texto: '{h.get_text().strip()}'")
        

    # 3. ACCEDER A HERMANOS (SIBLINGS):
    # Encuentra el primer artículo (article con id 'post-1')
    # Luego, navega al siguiente hermano adyacente usando .next_sibling o .find_next_sibling()
    print("\n--- 3. Encontrar Elementos Hermanos ---")
    post_1 = sopa.find('article', id='post-1')
    if post_1:
        # TODO: Usa .find_next_sibling('article') para encontrar el siguiente artículo
        post_2 = post_1.find_next_sibling()
        if post_2:
             titulo_post2 = post_2.find('h2').get_text().strip()
             print("Siguiente artículo encontrado:", titulo_post2)
             print("ID del Hermano:", post_2.get('id'))
        


if __name__ == "__main__":
    ejercicio_3_navegacion()
