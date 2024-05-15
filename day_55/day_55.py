from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return ('<h1 style="text-align:center;">Hello</h1>'
            '<p> This is a paragraph </p>')


@app.route("/bye")
def bye():
    return "Bye!.."


@app.route("/<name>")
def greet(name):
    return f"Hello there, {name}"



if __name__ == "__main__":
    app.run(debug=True)