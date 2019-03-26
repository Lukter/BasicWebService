#!/usr/bin/python

import int2word
from flask import Flask, jsonify

app = Flask(__name__)


def validatePath(path):
    try:
        path_as_integer = int(path)
        print('Path is ok!')
        return True
    except ValueError:
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

    return validatePath(path) and validateRange(path)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):

    if validateRequest(path):
        return jsonify(int2word.writter(path))
    else:
        return jsonify({"ERRO": 'Cannot resolve'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
