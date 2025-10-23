from flask import Flask, render_template, request, abort, jsonify, redirect,url_for
import math
from models import Produto

app = Flask(__name__)
produto = Produto()




@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("404.html"), 404




@app.route("/adicionar", methods = ["POST"])
def adicionar():
    nome = request.form["nome"]
    preco = float(request.form["preco"])
    produto.adicionar_produto(nome, preco)
    return redirect(url_for("listar_produtos"))



@app.route("/remover", methods = ["POST"])
def remover():
    nome = request.form["nome"]
    produto.remover_produto(nome)
    return redirect(url_for("listar_produtos"))




@app.route("/produtos")
def listar_produtos():
    return render_template("produtos.html", produtos = produto._PRODUTOS)



@app.route("/api")
def api():
    return jsonify(produto._PRODUTOS)

@app.route('/produtos_paginados')
def listar_produtos_paginados():
    return render_template('produtos_paginados.html')



@app.route("/produto/<int:produto_id>")
def detalhe_produto(produto_id):
    produto_encontrado = produto.achar_produtos(produto_id)
    if produto_encontrado is None:
        abort(404)
    return render_template("detalhe_produto.html", produto = produto_encontrado)

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome', "").lower()
    resultado = [p for p in  produto._PRODUTOS if nome_produto in p['nome'].lower()]

    return jsonify({'produtos_encontrados': resultado})





if __name__ == "__main__":
    app.run(debug=True)