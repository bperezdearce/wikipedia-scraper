import sqlite3

conn = sqlite3.connect("wikipedia.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM articulos")
num_filas = cursor.fetchone()[0]
print(f"Total de artículos en la base de datos: {num_filas}")

conn.close()