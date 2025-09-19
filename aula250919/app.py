from flask import Flask,render_template, abort, request, flash, redirect, url_for

app = Flask(__name__)


app.config['SECRET_KEY'] = "456743785t24783564738564783"


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/area-restrita")
def area_restrita():
    print ("Tentativa de acesso à área restrita sem autorização.")
    abort(401)




@app.route("/painel-admin")
def painel_admin():

    #aqui haveria uma verificação para ver se o usuário logado é um administrador

    print("Tentativa de acesso ao painel de administradorin sem permissão.")
    abort(403)
    
    
@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template("error404.html"), 404




@app.errorhandler(401)
def nao_autorizado(error):
    return render_template("error401.html"), 401




@app.errorhandler(403)
def acesso_proibido(error):
    return render_template("error403.html"),403


@app.route("/formulario", methods = ["GET", "POST"])
def formulario():
    if request.method == "POST":
        #Aqui ocorreria a validação
        nome = request.form.get("nome")
        email = request.form.get("email")
        print(f"dados recebidos do formulario: nome={nome}, Email={email}")
        #mensagem de sucesso
        flash(f"Obrigado por se cadastrar, {nome}!", "success")
        return redirect(url_for("formulario"))
    return render_template("formulario.html")



if __name__=="__main__":
    app.run(debug=True)