from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    data = requests.get('https://official-joke-api.appspot.com/random_joke')

    joke = data.json()

    return render_template("index.html", joke=joke)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
