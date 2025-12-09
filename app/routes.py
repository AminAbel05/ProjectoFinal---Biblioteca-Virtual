from flask import Blueprint, render_template, request, redirect, url_for
from .database import db_conexion

main = Blueprint("main", __name__)

# Leer - lista de libros
@main.route("/")
def index():
    conexion = db_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conexion.close()
    return render_template("index.html", libros=libros)

# Crear Nueva Tabla
@main.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]

        conexion = db_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO libros (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conexion.commit()
        conexion.close()

        return redirect(url_for("main.index"))
    
    return render_template("crear.html")

# Editar
@main.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conexion = db_conexion()
    cursor = conexion.cursor()

    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]

        cursor.execute("UPDATE libros SET nombre=?, precio=? WHERE id=?", (nombre, precio, id))
        conexion.commit()
        conexion.close()
        return redirect(url_for("main.index"))

    cursor.execute("SELECT * FROM libros WHERE id=?", (id,))
    libro = cursor.fetchone()
    conexion.close()

    return render_template("editar.html", libro=libro)

# Borrar
@main.route("/eliminar/<int:id>")
def eliminar(id):
    conexion = db_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

    return redirect(url_for("main.index"))