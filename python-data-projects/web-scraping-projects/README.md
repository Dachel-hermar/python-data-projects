<<<<<<< HEAD
# Aprende Web Scraping con BeautifulSoup 🍜

¡Bienvenido a este taller de ejercicios prácticos! Este repositorio está diseñado de forma modular para que aprendas, paso a paso, a extraer y procesar datos estructurados de páginas web usando **BeautifulSoup** en Python.

---

## 🛠️ Requisitos e Instalación

Para ejecutar los ejercicios, asegúrate de tener instalado Python 3.8 o superior. Luego, sigue estos pasos:

1. **Instalar dependencias**:
   Instala BeautifulSoup y el parser `lxml` ejecutando:
   ```bash
   pip install -r requirements.txt
   ```

2. **Estructura del Proyecto**:
   - `mock_pages/`: Contiene archivos HTML estáticos locales (`e_commerce.html`, `blog.html`, `books_table.html`) que simulan páginas web reales. Usar archivos locales te permite practicar de forma segura, rápida y sin depender de conexión a internet.
   - `ejercicios/`: Contiene los scripts de Python con tareas guiadas. Busca los comentarios `# TODO` para completarlos.
   - `soluciones/`: Contiene las respuestas completas de cada ejercicio para que puedas comparar y comprobar tu progreso.

---

## 📚 Ruta de Aprendizaje (Ejercicios)

Sigue los ejercicios en el orden recomendado:

### 1. [01_introduccion.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/01_introduccion.py)
* **Concepto**: Cómo cargar código HTML (desde strings y archivos locales) y parsearlo.
* **Métodos clave**: `BeautifulSoup()`, `find()`, `find_all()`, `.text`, `.get_text()`.

### 2. [02_atributos_y_selectores.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/02_atributos_y_selectores.py)
* **Concepto**: Filtrar por clases CSS, buscar atributos específicos (como enlaces `href` o imágenes `src`), y utilizar selectores CSS como en el diseño web moderno.
* **Métodos clave**: `find(class_="...")`, `.get('atributo')`, `select()`, `select_one()`.

### 3. [03_navegacion.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/03_navegacion.py)
* **Concepto**: Navegar por el árbol del documento DOM. Cómo acceder a elementos padres, hijos y hermanos de forma relativa.
* **Métodos clave**: `.parent`, `.children`, `.next_sibling`, `.previous_sibling`.

### 4. [04_tablas_y_listas.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/04_tablas_y_listas.py)
* **Concepto**: Extraer datos estructurados de tablas HTML (`<table>`, `<tr>`, `<td>`).
* **Objetivo**: Limpiar datos tabulados y convertirlos en listas de diccionarios de Python.

### 5. [05_proyecto_ecommerce.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/05_proyecto_ecommerce.py) (Proyecto)
* **Concepto**: Integrar todo lo aprendido.
* **Objetivo**: Extraer títulos, precios, opiniones y disponibilidad de productos del e-commerce local y guardarlos en un archivo estructurado `productos.json` o `productos.csv`.

### 6. [06_proyecto_blog.py](file:///c:/Users/Yoga%2012/OneDrive/Documentos/python/Extratcting%20data/BeautifulSoup/ejercicios/06_proyecto_blog.py) (Proyecto)
* **Concepto**: Búsquedas condicionales y filtrado.
* **Objetivo**: Extraer los posts del blog, categorizarlos según sus etiquetas y generar informes agregados sobre los autores.

---

## ⚡ Consejos Rápidos

* **Parsers**: En este curso usaremos tanto `html.parser` (el analizador nativo de Python) como `lxml` (que es mucho más rápido y maneja mejor el HTML mal estructurado).
* **Inspeccionar HTML**: Abre los archivos en `mock_pages/` en tu navegador y haz clic derecho en "Inspeccionar elemento" para entender la estructura antes de escribir código.
=======
# Big Data Portfolio – Dachel Hernández

¡Bienvenido a mi portafolio de proyectos de Big Data!

Este repositorio contiene los proyectos que he desarrollado como parte de mi formación en el máster de análisis de datos, con un enfoque práctico orientado tanto al entorno profesional como a la creación de soluciones reales para mi futura empresa tecnológica.

## 🧠 Objetivos
- Aplicar de forma práctica los conocimientos adquiridos en cada módulo avanzado del máster.
- Demostrar habilidades técnicas en herramientas Big Data (Hadoop, Spark, Kafka, NoSQL, Machine Learning...).
- Crear una base de proyectos reales orientados a negocio y optimización de datos.

## 📁 Estructura del Portafolio
Cada carpeta corresponde a un módulo o área temática. Dentro de cada una encontrarás:
- Un `README.md` con la descripción del proyecto
- Código fuente comentado
- Resultados o visualizaciones
- Reflexiones personales y aprendizajes clave

## 🚀 Próximos pasos
- [x] Crear repositorio y estructura inicial
- [ ] Subir los archivos
- [ ] Documentar aprendizajes de cada etapa
- [ ] Sincronizar con mi dashboard de Notion

---

Gracias por visitar este portafolio. ¡Estoy en constante aprendizaje y crecimiento!

>>>>>>> 3425af55c15bd5636d4e34f22a25e2c51881e357
