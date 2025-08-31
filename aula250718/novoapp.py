from flask import Flask, render_template

app =Flask(__name__)

@app.route("/")
def home():
    return render_template("qualquercoisa.html")

@app.route("/index")
def index():
    return render_template("index.html", app_name="Jorge")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)
