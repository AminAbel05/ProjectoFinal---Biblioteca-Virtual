from flask import Flask

app = Flask(__name__)

@app.route("/")
def Inicio():
    return "Hola mundo asi formalito XD"

if __name__ == "__main__":
    app.run(debug = True, port = 5000)