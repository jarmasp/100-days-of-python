from flask import Flask
import random as rd

app = Flask(__name__)

random_number = rd.randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
        "<img src='https://media.giphy.com/media/UsScA3f8ZvCEDYn0NI/giphy-downsized-large.gif'/>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess == random_number:
        return "<h1>You found me!</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtgRk3CEQLqOFd6/giphy.gif'/>"
    elif guess > random_number:
        return "<h1>Too high, try again!</h1>" \
        "<img src='https://media.giphy.com/media/qoWxwSCZIZzEPtfm4a/giphy.gif'/>"
    elif guess < random_number:
        return "<h1>Too low, try again!</h1>" \
        "<img src='https://media.giphy.com/media/l0NwuwTMoK1DLEhry/giphy.gif'/>"

if __name__ == "__main__":
    app.run(debug=True)