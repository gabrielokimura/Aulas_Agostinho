from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    produtos = ["maçã", "banana", "Laranja"]

    logado =True

    return render_template("home.html", produtos=produtos, logado=logado)