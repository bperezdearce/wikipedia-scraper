# Wikipedia Scraper

Este es un scraper de Wikipedia desarrollado con **Scrapy** y **BeautifulSoup**. Extrae los títulos, primeros párrafos y enlaces de los **primeros 10 artículos destacados** en Wikipedia en español.

## Características

- Extrae los primeros 10 artículos destacados.
- Obtiene el título y el primer párrafo de cada artículo.
- Guarda los datos en **JSON, CSV y SQLite**.
- Limpieza automática de espacios invisibles y referencias numéricas.

## Requisitos

Asegúrate de tener instalado:
- Python 3.8+ 🐍
- Scrapy (pip install scrapy)
- BeautifulSoup (pip install beautifulsoup4)
- Pandas (pip install pandas)
- Git (para clonar el repositorio)

## Instalación

1️⃣ Clona este repositorio:
```
git clone https://github.com/bperezdearce/wikipedia-scraper.git
cd wikipedia-scraper
```
2️⃣ Crea un entorno virtual (opcional, recomendado):
```
python -m venv .venv
source .venv/bin/activate  # En Mac/Linux
.venv\Scripts\activate  # En Windows
```
3️⃣ Instala las dependencias:
```
pip install -r requirements.txt
```

## Cómo Ejecutarlo

#### Ejecutar el scraper y guardar los datos
Para extraer los datos y guardarlos en JSON:
```
scrapy crawl wikipedia -o articulos.json
```
Para guardar los datos en CSV:
```
scrapy crawl wikipedia -o articulos.csv
```
## Exportar los Datos a SQL

#### 1. Crear la base de datos y la tabla
```
python db.py
```
Esto guardará los datos en wikipedia.db en una tabla llamada articulos.

#### 2. Consultar los datos en SQLite
Abre la base de datos en la terminal:
```
sqlite3 wikipedia.db
```
Luego, en la consola de SQLite, ejecuta:
```
SELECT * FROM articulos;
```
## Ejemplo de Salida JSON
```
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
```

## Posibles Mejoras

- Mejorar la extracción de más secciones de Wikipedia.
- Optimizar la limpieza de datos con Scrapy Pipelines.
- Añadir una API para consultar los datos fácilmente.


