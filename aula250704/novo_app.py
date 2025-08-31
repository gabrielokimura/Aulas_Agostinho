from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)

USUARIO_CADASTRADO="admin"
SENHA_CADASTRADA="123"


@app.route("/login", methods=["GET", "POST"])
def login():
    mensagem=""
    if request.method=="POST":
        usuario=request.form["username"]
        senha=request.form["password"]

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie("username", usuario, max_age=60*10)

            return resposta
        else:
            #Texto com aspas simples 
            mensagem="Usuário ou senha inválido. Tente novamente."

    return render_template('login.html', error=mensagem)


@app.route("/bemvindo", methods=["GET", "POST"])
def bemvindo():
    username = request.cookies.get('username')
    fundo=None
    if request.method=="POST":
        cor =request.method["cor"]
        fundo = make_response(redirect(url_for('bemvindo')))

        fundo.set_cookie("username", cor, max_age=60*10)



    if not username:
        return redirect(url_for("login"))
    
    return render_template("bemvindo.html", user=username, fundo=fundo)


@app.route("/logout")
def logout():
    resposta = make_response(redirect(url_for("login")))

    resposta.set_cookie("username", "", expires = 0)

    return resposta

if __name__=="__main__":
    app.run(debug=True)