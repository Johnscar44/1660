from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def index():
    headline = "This Is My Application!"
    return render_template("index.html", headline=headline)

@app.route("/list")

def list():
    Pokemon = ["Pikachu", "Charizard", "Squirtle", "Jigglypuff", "Bulbasaur",
    "Gengar", "Charmander", "Mew", "Lugia", "Gyarados"]
    return render_template("index.html", Pokemon=Pokemon)
