# -*- coding: utf-8 -*-
"""
Ejercicio 6: Proyecto Integrador Blog
--------------------------------------
En este proyecto de scraping avanzado trabajarás sobre mock_pages/blog.html.
Tu objetivo es extraer los artículos, categorizarlos, analizar las estadísticas
del blog y generar un reporte.

Tu tarea:
1. Extraer todos los posts de la lista de artículos (`article.post-card`).
   De cada post, debes extraer:
   - ID (`id` del elemento article).
   - Título.
   - Enlace completo al artículo.
   - Autor (de la etiqueta `.author`).
   - Fecha de publicación (de `.date` u obtener el atributo `datetime` de la etiqueta `time`).
   - Lista de etiquetas asociadas (clase `.tag`).
2. Implementar funciones para:
   - Contar cuántos posts ha escrito cada autor.
   - Buscar y listar posts que contengan una etiqueta específica (ej: 'Python').
3. Generar un reporte final por pantalla que resuma estas estadísticas.
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

    # 1. Extraer los artículos (.post-card)
    # TODO: articulos = ...
    articulos = sopa.find_all('article', class_='post-card')
    print(f"Se encontraron {len(articulos)} artículos en el blog.")

    for art in articulos:
        # TODO: Extraer datos
        # - ID
        id_post = art.get('id')
        print("Artículo contenedor (ID):", id_post)
        # - Título
        titulo = art.find('h2', class_='post-title').find('a')
        titulo_art = titulo.text.strip() if titulo else "No tiene Título"
        print("Los titulos de los ariculos:", titulo_art)
        # - Enlace
        enlace_post = titulo.get("href")
        print("Los enlaces de post:", enlace_post)
        # - Autor
        autor_tag = art.find('span', class_='author')
        autor = autor_tag.text.strip() if autor_tag else "No existe el autor"
        print("El autor del blog es:",autor)
        # - Fecha (texto legible y atributo 'datetime' de la etiqueta <time>)
        fecha_tag = art.find('time', class_='date')
        fecha_texto = ""
        fecha_iso = ""
        if fecha_tag:
            fecha_texto = fecha_tag.text.strip()
            fecha_iso = fecha_tag.get('datetime', '')
        print("La fecha del post es:", fecha_tag)

        # - Etiquetas (Pista: puede haber múltiples etiquetas por post. Búscalas con find_all o select)
        tags_tags = art.find_all('a', class_='tag')
        etiquetas = [tag.text.strip() for tag in tags_tags]
        print("Las Etiquetas son:", etiquetas)
        post = {
            "id": id_post,
            "titulo": titulo_art,
             "enlace": enlace_post,
             "autor": autor,
             "fecha_texto": fecha_texto,
             "fecha_iso": fecha_iso,
             "etiquetas": etiquetas # Lista de strings
         }
        posts.append(post)
        pass

    print(f"Total artículos extraídos: {len(posts)}\n")

    # 2. Análisis y Filtrado de Datos
    
    # TODO: A) Contar posts por autor
    # Genera un diccionario donde las claves sean los autores y los valores la cantidad de posts que escribieron.
    autores_count = {}
    for p in posts:
        """Si el autor ya existe en el diccionario, suma 1 a su contador. 
        Si no, inicializa su contador en 1."""
        autor = p["autor"]
        autores_count[autor] = autores_count.get(autor, 0) + 1 # Si el autor ya existe, suma 1. Si no, inicializa en 1.

    print("Artículos por autor:")
    for autor, cantidad in autores_count.items():
        print(f"  - {autor}: {cantidad}")

    # TODO: B) Buscar posts con la etiqueta 'Python'
    # Filtra la lista 'posts' para obtener sólo aquellos que tengan 'Python' en su lista de etiquetas.
    # Guarda estos posts en una nueva lista llamada 'python_posts' y luego imprímelos.
    
    python_posts = []
    
    for p in posts:
       
        """Si 'Python' está en la lista de etiquetas del post, 
        añádelo a la lista python_posts."""
        
        if 'Python' in p["etiquetas"]:
            python_posts.append(p)
    tag_buscada = 'Python'

    

    print("\nArtículos con etiqueta 'Python':")

    for p in python_posts:
        """Imprime el título y autor de cada post que tenga la etiqueta 'Python'."""
        print(f"  * {p['titulo']} (por {p['autor']})") 


if __name__ == "__main__":
    scraping_blog()
