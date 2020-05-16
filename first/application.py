<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template
>>>>>>> 623f213f28b3c58e43bceb35be483fb8f950c2b3

app = Flask(__name__)

@app.route("/")
<<<<<<< HEAD
def index():
    return render_template("index.html")
=======

def index():
    headline = "This Is My Application!"
    return render_template("index.html", headline=headline)

@app.route("/list")

def list():
    Pokemon = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff", "Bulbasaur",
    "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    return render_template("index.html", Pokemon=Pokemon)
>>>>>>> 623f213f28b3c58e43bceb35be483fb8f950c2b3
