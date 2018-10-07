import json
from flask import Flask, jsonify
from src.ipcontainer import IPContainer

app = Flask(__name__)

@app.route("/")
def hello():
    return "works :-)"

if __name__ == "__main__":
    app.run()