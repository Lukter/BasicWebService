#!/usr/bin/python

from flask import Flask,jsonify

app = Flask(__name__)


def validatePath(path):
    try:
        path_as_integer = int(path)
        print('Path is ok!')
        return True
    except ValueError as e:
        print('Invalid path! Cannot resolve...')
        return False

def validateRange(path):
    path_as_integer = int(path)
    if -99999 <= path_as_integer <= 99999:
        print('Number in a valid range!')
        return True
    else:
        print('Invalid number request! Cannot resolve...')
        return False

def validateRequest(path):
    if not validatePath(path):
        return False

    if not validateRange(path):
        return False

    return True

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    
    if validateRequest(path):
        path = int(path)
        return jsonify({"extenso": path})
    else:
        return jsonify({"ERRO": path})

if __name__ == '__main__':
    app.run()
