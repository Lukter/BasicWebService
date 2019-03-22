#!/usr/bin/python

import int2word
from flask import Flask,jsonify

app = Flask(__name__)

UNIT = {'00': '', '01': 'um', '02': 'dois', '03': 'tres', '04': 'quatro', '05': 'cinco',
        '06': 'seis', '07': 'sete', '08': 'oito', '09': 'nove', '10': 'dez', '11': 'onze',
        '12': 'doze', '13': 'treze', '14': 'quatorze', '15': 'quinze', '16': 'dezesseis',
        '17': 'dezessete', '18': 'dezoito', '19': 'dezenove'}

TENS = {'0': '', '2': 'vinte', '3': 'trinta', '4': 'quarenta', '5': 'cinquenta', '6': 'sessenta',
        '7': 'setenta', '8': 'oitenta', '9': 'noventa'}

HUNDRED = {'0': '', '1': 'cento', '2': 'duzentos', '3': 'trezentos', '4': 'quatrocentos', '5': 'quinhentos',
           '6': 'seiscentos', '7': 'setecentos', '8': 'oitocentos', '9': 'novecentos'}

THOUSAND = {'00': '', '01': 'mil'}

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
        return jsonify(int2word.writter(path))
    else:
        return jsonify({"ERRO": 'Cannot resolve'})

if __name__ == '__main__':
    app.run()
