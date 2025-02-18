import sqlite3
import pandas as pd

conn = sqlite3.connect("wikipedia.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM articulos")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS articulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        primer_parrafo TEXT,
        url TEXT
    )
""")

df = pd.read_csv("articulos.csv", names=["titulo", "primer_parrafo", "url"], encoding="utf-8")
df.to_sql("articulos", conn, if_exists="append", index=False)

conn.commit()
conn.close()