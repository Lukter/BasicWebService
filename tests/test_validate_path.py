import sys
sys.path.append('../source/')

import int2word
import requests
import json

result = requests.get('http://localhost:5000/00000')
assert(result.json() == {'extenso': 'zero'})

result = requests.get('http://localhost:5000/00001')
assert(result.json() == {'extenso': 'um'})


result = requests.get('http://localhost:5000/00010')
assert(result.json() == {'extenso': 'dez'})

result = requests.get('http://localhost:5000/00015')
assert(result.json() == {'extenso': 'quinze'})

result = requests.get('http://localhost:5000/00020')
assert(result.json() == {'extenso': 'vinte'})


result = requests.get('http://localhost:5000/00021')
assert(result.json() == {'extenso': 'vinte e um'})

result = requests.get('http://localhost:5000/00100')
assert(result.json() == {'extenso': 'cem'})

result = requests.get('http://localhost:5000/00101')
assert(result.json() == {'extenso': 'cento e um'})

result = requests.get('http://localhost:5000/00110')
assert(result.json() == {'extenso': 'cento e dez'})

result = requests.get('http://localhost:5000/00115')
assert(result.json() == {'extenso': 'cento e quinze'})

result = requests.get('http://localhost:5000/00120')
assert(result.json() == {'extenso': 'cento e vinte'})

result = requests.get('http://localhost:5000/00130')
assert(result.json() == {'extenso': 'cento e trinta'})

result = requests.get('http://localhost:5000/00131')
assert(result.json() == {'extenso': 'cento e trinta e um'})

result = requests.get('http://localhost:5000/00200')
assert(result.json() == {'extenso': 'duzentos'})

result = requests.get('http://localhost:5000/00201')
assert(result.json() == {'extenso': 'duzentos e um'})

result = requests.get('http://localhost:5000/00210')
assert(result.json() == {'extenso': 'duzentos e dez'})

result = requests.get('http://localhost:5000/00215')
assert(result.json() == {'extenso': 'duzentos e quinze'})

result = requests.get('http://localhost:5000/00220')
assert(result.json() == {'extenso': 'duzentos e vinte'})

result = requests.get('http://localhost:5000/00221')
assert(result.json() == {'extenso': 'duzentos e vinte e um'})

result = requests.get('http://localhost:5000/01000')
assert(result.json() == {'extenso': 'mil'})

result = requests.get('http://localhost:5000/01001')
assert(result.json() == {'extenso': 'mil e um'})

result = requests.get('http://localhost:5000/01010')
assert(result.json() == {'extenso': 'mil e dez'})

result = requests.get('http://localhost:5000/01011')
assert(result.json() == {'extenso': 'mil e onze'})

result = requests.get('http://localhost:5000/01020')
assert(result.json() == {'extenso': 'mil e vinte'})

result = requests.get('http://localhost:5000/01025')
assert(result.json() == {'extenso': 'mil e vinte e cinco'})

result = requests.get('http://localhost:5000/01100')
assert(result.json() == {'extenso': 'mil e cem'})

result = requests.get('http://localhost:5000/01101')
assert(result.json() == {'extenso': 'mil cento e um'})

result = requests.get('http://localhost:5000/01110')
assert(result.json() == {'extenso': 'mil cento e dez'})

result = requests.get('http://localhost:5000/01115')
assert(result.json() == {'extenso': 'mil cento e quinze'})

result = requests.get('http://localhost:5000/01120')
assert(result.json() == {'extenso': 'mil cento e vinte'})

result = requests.get('http://localhost:5000/01125')
assert(result.json() == {'extenso': 'mil cento e vinte e cinco'})

result = requests.get('http://localhost:5000/01200')
assert(result.json() == {'extenso': 'mil e duzentos'})

result = requests.get('http://localhost:5000/01201')
assert(result.json() == {'extenso': 'mil duzentos e um'})

result = requests.get('http://localhost:5000/02000')
assert(result.json() == {'extenso': 'dois mil'})

result = requests.get('http://localhost:5000/02001')
assert(result.json() == {'extenso': 'dois mil e um'})

result = requests.get('http://localhost:5000/02010')
assert(result.json() == {'extenso': 'dois mil e dez'})

result = requests.get('http://localhost:5000/02100')
assert(result.json() == {'extenso': 'dois mil e cem'})

result = requests.get('http://localhost:5000/02101')
assert(result.json() == {'extenso': 'dois mil cento e um'})

result = requests.get('http://localhost:5000/02101')
assert(result.json() == {'extenso': 'dois mil cento e um'})

result = requests.get('http://localhost:5000/02201')
assert(result.json() == {'extenso': 'dois mil duzentos e um'})

result = requests.get('http://localhost:5000/11201')
assert(result.json() == {'extenso': 'onze mil duzentos e um'})


result = requests.get('http://localhost:5000/20201')
assert(result.json() == {'extenso': 'vinte mil duzentos e um'})

result = requests.get('http://localhost:5000/25201')
assert(result.json() == {'extenso': 'vinte e cinco mil duzentos e um'})

result = requests.get('http://localhost:5000/10000')
assert(result.json() == {'extenso': 'dez mil'})

result = requests.get('http://localhost:5000/-00000')
assert(result.json() == {'extenso': 'zero'})

result = requests.get('http://localhost:5000/-99999')
assert(result.json() == {'extenso': 'menos noventa e nove mil novecentos e noventa e nove'})


result = requests.get('http://localhost:5000/1')
assert(result.json() == {'extenso': 'um'})

result = requests.get('http://localhost:5000/0')
assert(result.json() == {'extenso': 'zero'})

result = requests.get('http://localhost:5000/1.1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/1,1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/-1')
assert(result.json() == {'extenso': 'menos um'})

result = requests.get('http://localhost:5000/-1.1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/-1,1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/9999999999999')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/-9999999999999')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/a')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/a1a1a1a1a1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/-a')
assert(result.json() == {'ERRO': 'Cannot resolve'})

result = requests.get('http://localhost:5000/-a1a1a1a1a1')
assert(result.json() == {'ERRO': 'Cannot resolve'})

print('PASSED ALL TESTS!')
