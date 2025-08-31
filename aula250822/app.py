from flask import Flask, render_template, redirect, url_for, request, make_response, session


app = Flask(__name__)

app.secret_key="123456789"

@app.route("/")
def pagina_inicial():
    return render_template("inicial.html")

@app.route("/capablanca")
def capablanca():
    return render_template("capablanca.html")

@app.route("/mikhail")
def mikhail():
    return render_template("mikhail.html")

@app.route("/fischer")
def fischer():
    return render_template("fischer.html")

@app.route("/kasparov")
def kasparov():
    return render_template("kasparov.html")

@app.route("/carlsen")
def carlsen():
    return render_template("carlsen.html")

if __name__== "__main__":
    app.run(debug=True)