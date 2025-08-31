from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = '234356876'

@app.route("/user/<nome>")
def nome(nome):
    return render_template("profile.html", user=nome)





@app.route("/login", methods=["POST"])
def login():
    username=request.form["username"]
    session["username"]=username
    return redirect(url_for("profile"))



@app.route("/lista")
def lista():
    produtos = ["Maçã", "Banana", "Laranja"]

    logado =True

    return render_template("logado.html", produtos=produtos, logado=logado)


@app.route("/profile")
def profile():
    if "username" in session:
        return f"<h1>Bem vindo de volta, (session['username']!</h1>)"
    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return "Você foi desligado"

@app.route("/")
def home():
    return "Página inicial. Faça login para acessar seu perfil"

@app.route("/")
def index():
    # A sessão está disponível globalmente nos templates
    return render_template("home.html")

if __name__ =="__main__":
    app.run(debug=True)
