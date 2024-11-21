from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Ocean Brasil! Eu amo o curso de dev ops</p>"

if __name__ == "__main__":
    app.run(debug=True)