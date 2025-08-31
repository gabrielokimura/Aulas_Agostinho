from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def inicial():
    #Casca padrão
    return render_template("index.html")

@app.route("/api/aluno")
def api_alunos():
    alunos=[
        {"nome": "Mario", "nota":7},
        {"nome":"Eduardo", "nota":10},
        {"nome": "Márcia", "nota":3}]
    return jsonify(alunos)

if __name__=="__main__":
    app.run(debug=True)