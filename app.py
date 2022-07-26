from flask import Flask, render_template 
app = Flask("hola")
# definimos ruta-raiz
@app.route("/")
def hola():
    return "Hola Mundo, paso inicial 278913677777"

@app.route("/meucontato")
def meucontato():
    return render_template("index.html")

