from flask import Flask, render_templates 
app = Flask("hola")
# definimos ruta-raiz
@app.route("/")
def hola():
    return "Hola Mundo, paso inicial 2789"

@app.route("/meucontato")
def meucontato():
    return render_templates("index.html")

