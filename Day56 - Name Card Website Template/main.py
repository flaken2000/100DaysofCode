from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Rendering HTML Elements
    return render_template("index.html")




if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)