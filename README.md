# Wikipedia Scraper 🕵️‍♀️

Este es un scraper de Wikipedia desarrollado con Scrapy y BeautifulSoup. Extrae los títulos, primeros párrafos y enlaces de los 10 artículos destacados en Wikipedia en español. 📜✨

🚀 Características

Extrae los primeros 10 artículos destacados.

Obtiene el título y el primer párrafo de cada artículo.

Guarda los datos en formato JSON.

Limpieza automática de espacios invisibles y referencias numéricas.

📌 Requisitos

Asegúrate de tener instalado:

Python 3.8+ 🐍

Scrapy (pip install scrapy)

BeautifulSoup (pip install beautifulsoup4)

Git (para clonar el repositorio)

🔧 Instalación

1️⃣ Clona este repositorio:

git clone https://github.com/bperezdearce/wikipedia-scraper.git
cd wikipedia-scraper

2️⃣ Crea un entorno virtual (opcional, recomendado):

python -m venv .venv
source .venv/bin/activate  # En Mac/Linux
.venv\Scripts\activate  # En Windows

3️⃣ Instala las dependencias:

pip install -r requirements.txt

🏃‍♀️ Cómo Ejecutarlo

Para ejecutar el scraper y guardar la salida en un archivo JSON:

scrapy crawl wikipedia -o articulos.json

Después de ejecutarlo, encontrarás un archivo articulos.json con los resultados.

📜 Ejemplo de Salida JSON

[
    {
        "titulo": "Carne",
        "primer_parrafo": "La carne es el tejido muscular de los animales que se consume como alimento...",
        "url": "https://es.wikipedia.org/wiki/Carne"
    },
    {
        "titulo": "Historia de la hamburguesa",
        "primer_parrafo": "Los orígenes de la hamburguesa son inciertos, pero se sabe que fue elaborada en el siglo XIX...",
        "url": "https://es.wikipedia.org/wiki/Historia_de_la_hamburguesa"
    }
]

💡 Posibles Mejoras

🔹 Exportar datos a CSV o base de datos.🔹 Mejorar la extracción de más secciones de Wikipedia.🔹 Implementar Scrapy Pipelines para limpiar los datos antes de guardarlos.
