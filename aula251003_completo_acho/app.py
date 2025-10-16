from flask import Flask, render_template, redirect, session, url_for, request
from models import UsuarioModel



usuario_model = UsuarioModel()
app =Flask(__name__)


@app.route("/usuarios")
def listar_usuarios():
    usuarios = usuario_model.get_todos()
    return render_template("usuarios.html",lista_usuarios = usuarios, mensagem = usuario_model.mensagem, mensagem2 = usuario_model.mensagem2)


@app.route("/usuarios/novo", methods = ["POST"])
def adicionar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    usuario_model.salvar(nome,email, senha)
    return redirect(url_for("listar_usuarios"))


@app.route("/usuarios/deletar", methods = ["POST"])
def deletar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    usuario_model.remover(nome,email)
    return redirect(url_for("listar_usuarios"))




@app.route("/usuarios/logar", methods = ["POST"])
def logar_usuario():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    usuario_model.logar(nome,email,senha)
    return redirect(url_for("listar_usuarios"))



if __name__=="__main__":
    app.run(debug=True)