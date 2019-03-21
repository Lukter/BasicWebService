#!/usr/bin/python

from flask import Flask,jsonify

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return jsonify({"message":"Hello Json!"})

if __name__ == '__main__':
    app.run()
