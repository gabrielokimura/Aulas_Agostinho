from flask import Flask, render_template, redirect, url_for, request, make_response, session

app = Flask(__name__)

USUARIO_CADASTRADO="Admin"
SENHA_CADASTRADA="123"
app.secret_key="vai"            

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
    if "contador" not in session:
        session['contador'] = 1
    

    lista_noticias = {"esporte": ["noticia1","noticia2","noticia3"],"entretenimento": ["noticia4","noticia5","noticia6"],"lazer": ["noticia7","noticia8","noticia9"],}
    username = request.cookies.get('username')
    fundo=None
    if request.method=="POST":
        session["categoria"]=None
        if "categoria" in request.form:
            session["categoria"] =  request.form["categoria"]
            
        
        elif session["categoria"]=="":
            session["categoria"]=None


        elif "cor" in request.form:
            fundo = request.form["cor"]
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie("cor", fundo, max_age=30*10)
            
            return resposta
            
    else:
        session['contador'] += 1
    
    if not username:
        return redirect(url_for("login"))
    
    return render_template("bemvindo.html", user=username, fundo=request.cookies.get("cor"), contador=session['contador'], noticias=lista_noticias, categoria=session["categoria"] )


@app.route("/logout")
def logout():
    resposta = make_response(redirect(url_for("login")))

    resposta.set_cookie("username", "", expires = 0)

    session["contador"]=0

    return resposta

if __name__=="__main__":
    app.run(debug=True)

# Utilizar http://127.0.0.1:5000/login