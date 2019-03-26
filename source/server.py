#!/usr/bin/python

import int2word
import logging
import os
from flask import Flask, jsonify

app = Flask(__name__)

def log():
    logger = logging.getLogger('server')
    hdlr = logging.FileHandler(os.path.join(os.path.dirname(__file__),
                               'server.log'))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)
    return logger

def validatePath(path):
    try:
        path_as_integer = int(path)
        logger.info("Path is ok!")
        return True
    except ValueError:
        logger.info('Invalid path! Cannot resolve...')
        return False


def validateRange(path):
    path_as_integer = int(path)
    if -99999 <= path_as_integer <= 99999:
        logger.info('Number in a valid range!')
        return True
    else:
        logger.info('Invalid number request! Cannot resolve...')
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

logger = log()
logger.info("Server Online")
if __name__ == '__main__':
    app.run(host='0.0.0.0')
