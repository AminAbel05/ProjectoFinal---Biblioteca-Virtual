import sqlite3
import os

db_main = "biblioteca.db"

def db_conexion():
    conexion = sqlite3.connect(db_main)
    conexion.row_factory = sqlite3.Row 
    return conexion

def init_db():
    if not os.path.exists(db_main):
        conexion = db_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            CREATE TABLE libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
            )
        """)

        conexion.commit()
        conexion.close()