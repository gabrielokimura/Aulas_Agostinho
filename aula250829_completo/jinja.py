from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicial():
    escolha=None
    if request.method=="POST":
        escolha=request.form["tabela"]

    alunos=[
    {"nome": "Mario", "nota":7},
    {"nome":"Eduardo", "nota":10},
    {"nome": "Márcia", "nota":3}]

    presenca=[
        {"nome": "Mario", "faltas":5},
        {"nome":"Eduardo", "faltas":55},
        {"nome": "Márcia", "faltas":0}]

    return render_template("jinja.html", alunos=alunos, escolha=escolha, presenca=presenca)

if __name__=="__main__":
    app.run(debug=True)