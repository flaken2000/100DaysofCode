from flask import Flask
import random
app = Flask(__name__)

HIGH_IMG = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_IMG = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT_IMG = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
GUESS_IMG = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"

random_number = random.randint(0, 9)
print(f"Random number is: {random_number}")


@app.route('/')
def hello_world():
    # Rendering HTML Elements
    return f"<h1>Guess a number between 0 and 9</h1><img src={GUESS_IMG}>"


@app.route('/<int:number>')
def guess_number(number):
    if number == random_number:
        return f"<h1 style='color:green'>You found me!</h1><img src={CORRECT_IMG}>"
    elif number < random_number:
        return f"<h1 style='color:red'>Too low, try again!</h1><img src={LOW_IMG}>"
    else:
        return f"<h1 style='color:magenta'>Too high, try again!</h1><img src={HIGH_IMG}>"


if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
