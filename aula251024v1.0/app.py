from flask import Flask, render_template, session, request, redirect, url_for
from models import *


modelo = UsuarioModel()
app = Flask(__name__)
app.secret_key = "erfgre7grtyuhe568jn97m67j98579h6798jy6gft847"


@app.route("/login", methods = ["GET","POST"])
def login ():
    mensagem = ""
    if request.method == "POST":
        session["nome"]=request.form.get("nome")
        session["senha"] = request.form.get("senha")
        nome = session["nome"]
        senha = session["senha"]
        tamanho = len(modelo.funcionarios)
        for i in range (tamanho):
            if modelo.funcionarios[i]["nome"] == nome and  modelo.funcionarios[i]["senha"] == senha:
                session["usuario"] = modelo.funcionarios[i]
                return redirect(url_for("logado"))
        mensagem = "Usuário ou senha inválidos"
    return render_template("login.html", mensagem = mensagem)
        



@app.route("/logado")
def logado():
    usuario = session.get("usuario")
    if not usuario:
        return redirect(url_for("login"))

    return render_template("logado.html", usuario = usuario, modelo = modelo)

    

    




@app.route("/remover_funcionario")
def remover_funcionario():
    if request.method == "POST":
        nome = request.form.get("nome")


if __name__ == "__main__":
    app.run(debug=True)