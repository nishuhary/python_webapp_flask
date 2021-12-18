import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/whats your name')
def face():
    return 'I\'m My-Simple_Webapp'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
