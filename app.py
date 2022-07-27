from flask import Flask, render_template 
from datetime import datetime
app = Flask("hola")

posts = [
    {
        "title": "Mi primer Post",
        "body": "Aqui o texto do Post",
        "author": "Feulo",
        "created":datetime(2022,7,25)
    },
     {
        "title": "Mi segundo Post",
        "body": "Aqui o texto do Post",
        "author": "Danilo",
        "created":datetime(2022,7,26)
    }
]

# definimos ruta-raiz
@app.route("/")
def hola():
    return render_template("index.html", posts = posts)

#@app.route('/login')

