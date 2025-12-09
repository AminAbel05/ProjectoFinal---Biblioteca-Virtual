# Projecto Final - Biblioteca Virtual
Haciendo uso de python, sqlite3 y flask creamons un proyecto de una biblioteca virtual en la que podemos agregar, eliminar o editar libros para que los usuarios puedan informarse de sus precios y valores para poder comprarlos en una tienda cerca

Biblioteca Virtual  
Aplicación web CRUD desarrollada con **Flask** y **SQLite3**, que permite gestionar libros de manera sencilla (crear, listar, actualizar y eliminar).  
Proyecto organizado de forma modular y funcionando sin SQLAlchemy.

----------------- Características principales -----------------

- CRUD completo de libros (Crear, Leer, Actualizar, Eliminar)
- Base de datos SQLite3 con esquema controlado mediante archivo `schema.sql`
- Proyecto modular utilizando Blueprints
- Formularios validados con Flask-WTF
- Plantillas HTML con Jinja2
- Estilos básicos con Bootstrap
- Estructura de proyecto profesional

----------------- Estructura del proyecto -----------------

<img width="168" height="359" alt="image" src="https://github.com/user-attachments/assets/f734f2f2-859a-4522-92b0-2e68a69ff86f" />


----------------- Requisitos previos -----------------

Debes tener instalado:
- Python 3.8 o superior  
- pip (incluido con Python)

----------------- Crear y activar entorno virtual -----------------

Windows:

python -m venv env
env\Scripts\activate

Linux/Mac:

python3 -m venv env
source env/bin/activate

Instalar dependencias

En tu entorno virtual ejecuta:
pip install -r requirements.txt

----------------- Crear la base de datos -----------------

Ejecuta este comando una vez:
sqlite3 database.db < schema.sql

Si quieres borrar todo y empezar de cero:
del database.db   # Windows
rm database.db    # Linux/Mac
sqlite3 database.db < schema.sql

----------------- Ejecutar la aplicación -----------------

Desde la raíz del proyecto busco el archivo python y correlo:
iniciar.py

Abre en tu navegador con la direccion web que tu entorno muestra:
por ejemplo: http://127.0.0.1:5000

----------------- Funcionalidades del CRUD -----------------

- /libros → Listar todos los libros
- /libros/nuevo → Crear un nuevo libro
- /libros/editar/<id> → Editar un libro
- /libros/eliminar/<id> → Eliminar un libro

Los formularios validan que:
El nombre no esté vacío
El precio sea un número válido

----------------- Migraciones (Manual) -----------------

Como no usamos SQLAlchemy, las migraciones se hacen así:
Editas schema.sql.

Si cambias tablas:
Borras database.db
Ejecutas de nuevo el schema.

Opcionalmente puedes agregar una carpeta:
migrations/
    001_create_tables.sql

----------------- Problemas comunes -----------------

- "cannot import name 'create_app' from 'app'"

Solución: Asegúrate de que __init__.py contiene:

def create_app():
    app = Flask(__name__)
    ...
    return app

- Flask no detecta templates

Verifica que la estructura sea:

app/templates/

----------------- Autores del Proyecto -----------------

Proyecto realizado por Candida Morfa y Amin Abel Amador Jimenez como parte de la práctica final del curso de Python Intermedio.

----------------- Licencia -----------------

Uso educativo – libre para mejorar, modificar o extender el uso de Flask en un entorno seguro.
