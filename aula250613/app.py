from flask import Flask, render_template

app = Flask(__name__)

@app.route("/user/<nome>")
def profile(nome):
    return render_template("profile.html", user=nome)





@app.route("/")
def home():
    produtos = ["maçã", "banana", "Laranja"]

    logado =True

    return render_template("home.html", produtos=produtos, logado=logado)


if __name__ =="__main__":
    app.run(debug=True)
