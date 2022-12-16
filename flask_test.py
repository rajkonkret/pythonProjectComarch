from flask import Flask, render_template

# pip install flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello"


@app.route("/salvador")
def salvador():
    return "Hello. Salvador"


if __name__ == "__main__":
    app.run(debug=True)
