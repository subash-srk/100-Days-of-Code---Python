from flask import Flask
import random

number = random.randint(0, 10)
print(number)

app = Flask(__name__)


@app.route("/")
def hl():
    return ('<h1>Guess a Number between 0 to 9</h1>'
            '<image src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route("/<int:url>")
def result(url):
    if url > number:
        return ('<h1>Too High</h1>'
            '<image src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

    elif url < number:
        return ('<h1>Too Low</h1>'
            '<image src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')

    else:
        return ('<h1>You got it! </h1>'
            '<image src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)