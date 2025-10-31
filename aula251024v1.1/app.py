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
    if request.args.get("mensagem") ==None:
        mensagem =""
    else:
        mensagem = request.args.get("mensagem")

    if request.args.get("mensagem2") ==None:
        mensagem2 =""
    else:
        mensagem2 = request.args.get("mensagem2")
    
    usuario = session.get("usuario")
    if not usuario:
        return redirect(url_for("login"))

    return render_template("logado.html", usuario = usuario, modelo = modelo,mensagem = mensagem, mensagem2=mensagem2)

    

    




@app.route("/remover_funcionario", methods = ["POST"])
def remover_funcionario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        modelo.remover_funcionario(nome,email)
        return redirect(url_for("logado"))
    



@app.route("/adicionar_funcionario", methods = ["POST"])
def adicionar_funcionario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        cargo = request.form.get("cargo")
        modelo.adicionar_funcionario(nome,email, senha, cargo)
        return redirect(url_for("logado"))
    


@app.route("/remover_hospede", methods = ["POST"])
def remover_hospede():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        modelo.remover_hospede(nome,cpf)
        return redirect(url_for("logado"))
    



@app.route("/adicionar_reserva", methods = ["POST"])
def adicionar_reserva():
    if request.method == "POST":
        id = request.form.get("id")
        numero_quarto = request.form.get("numero_quarto")
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        status = request.form.get("status")
        mensagem = modelo.adicionar_reserva(id,numero_quarto, checkin, checkout, status)
        return redirect(url_for("logado", mensagem=mensagem))
    


@app.route("/adicionar_hospede", methods = ["POST"])
def adicionar_hospede():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        cpf = request.form.get("cpf")
        telefone = request.form.get("telefone")
        modelo.adicionar_hospede(nome,cpf, telefone, email)
        return redirect(url_for("logado"))
    

@app.route("/alterar_reserva", methods=["POST"])
def alterar_reserva():
    if request.method == "POST":
        id_antigo = request.form.get("id_antigo")
        id_hospede = request.form.get("id")
        numero_quarto = request.form.get("numero_quarto")
        checkin = request.form.get("checkin")
        checkout = request.form.get("checkout")
        status = request.form.get("status")
        mensagem = modelo.alterar_reserva(id_antigo,id_hospede,numero_quarto, checkin, checkout, status)
        return redirect(url_for("logado", mensagem2=mensagem))
    


@app.route("/atualizar_quarto", methods = ["POST"])
def atualizar_quarto():
    if request.method == "POST":
        id = request.form.get("id")
        numero = request.form.get("numero")
        tipo = request.form.get("tipo")
        capacidade = request.form.get("capacidade")
        preco_diaria = request.form.get("preco_diaria")
        descricao = request.form.get("descricao")
        status = request.form.get("status")
        localizacao = request.form.get("localizacao")
        disponivel = request.form.get("disponivel")
        modelo.atualizar_quarto(id,numero,tipo,capacidade,preco_diaria,descricao,status,localizacao,disponivel)
        return redirect(url_for("logado"))
    



@app.route("/atualizar_status_quarto", methods = ["POST"])
def atualizar_status_quarto():
    if request.method =="POST":
        numero = request.form.get("numero")
        print(numero)
        status = request.form.get("status")
        print(status*10)
        modelo.atualizar_status_quarto(numero, status)
        return redirect(url_for("logado"))





if __name__ == "__main__":
    app.run(debug=True)