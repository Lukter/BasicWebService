import sys
sys.path.append('../source/')

import int2word

result = int2word.writter('00000')
assert(result == {'extenso': 'zero'})

result = int2word.writter('00001')
assert(result == {'extenso': 'um'})


result = int2word.writter('00010')
assert(result == {'extenso': 'dez'})

result = int2word.writter('00015')
assert(result == {'extenso': 'quinze'})

result = int2word.writter('00020')
assert(result == {'extenso': 'vinte'})


result = int2word.writter('00021')
assert(result == {'extenso': 'vinte e um'})

result = int2word.writter('00100')
assert(result == {'extenso': 'cem'})

result = int2word.writter('00101')
assert(result == {'extenso': 'cento e um'})

result = int2word.writter('00110')
assert(result == {'extenso': 'cento e dez'})

result = int2word.writter('00115')
assert(result == {'extenso': 'cento e quinze'})

result = int2word.writter('00120')
assert(result == {'extenso': 'cento e vinte'})

result = int2word.writter('00130')
assert(result == {'extenso': 'cento e trinta'})

result = int2word.writter('00131')
assert(result == {'extenso': 'cento e trinta e um'})

result = int2word.writter('00200')
assert(result == {'extenso': 'duzentos'})

result = int2word.writter('00201')
assert(result == {'extenso': 'duzentos e um'})

result = int2word.writter('00210')
assert(result == {'extenso': 'duzentos e dez'})

result = int2word.writter('00215')
assert(result == {'extenso': 'duzentos e quinze'})

result = int2word.writter('00220')
assert(result == {'extenso': 'duzentos e vinte'})

result = int2word.writter('00221')
assert(result == {'extenso': 'duzentos e vinte e um'})

result = int2word.writter('01000')
assert(result == {'extenso': 'mil'})

result = int2word.writter('01001')
assert(result == {'extenso': 'mil e um'})

result = int2word.writter('01010')
assert(result == {'extenso': 'mil e dez'})

result = int2word.writter('01011')
assert(result == {'extenso': 'mil e onze'})

result = int2word.writter('01020')
assert(result == {'extenso': 'mil e vinte'})

result = int2word.writter('01025')
assert(result == {'extenso': 'mil e vinte e cinco'})

result = int2word.writter('01100')
assert(result == {'extenso': 'mil e cem'})

result = int2word.writter('01101')
assert(result == {'extenso': 'mil cento e um'})

result = int2word.writter('01110')
assert(result == {'extenso': 'mil cento e dez'})

result = int2word.writter('01115')
assert(result == {'extenso': 'mil cento e quinze'})

result = int2word.writter('01120')
assert(result == {'extenso': 'mil cento e vinte'})

result = int2word.writter('01125')
assert(result == {'extenso': 'mil cento e vinte e cinco'})

result = int2word.writter('01200')
assert(result == {'extenso': 'mil e duzentos'})

result = int2word.writter('01201')
assert(result == {'extenso': 'mil duzentos e um'})

result = int2word.writter('02000')
assert(result == {'extenso': 'dois mil'})

result = int2word.writter('02001')
assert(result == {'extenso': 'dois mil e um'})

result = int2word.writter('02010')
assert(result == {'extenso': 'dois mil e dez'})

result = int2word.writter('02100')
assert(result == {'extenso': 'dois mil e cem'})

result = int2word.writter('02101')
assert(result == {'extenso': 'dois mil cento e um'})

result = int2word.writter('02101')
assert(result == {'extenso': 'dois mil cento e um'})

result = int2word.writter('02201')
assert(result == {'extenso': 'dois mil duzentos e um'})

result = int2word.writter('11201')
assert(result == {'extenso': 'onze mil duzentos e um'})


result = int2word.writter('20201')
assert(result == {'extenso': 'vinte mil duzentos e um'})


result = int2word.writter('25201')
assert(result == {'extenso': 'vinte e cinco mil duzentos e um'})

result = int2word.writter('10000')
assert(result == {'extenso': 'dez mil'})

result = int2word.writter('-00000')
assert(result == {'extenso': 'zero'})

result = int2word.writter('-99999')
assert(result == {'extenso': 'menos noventa e nove mil novecentos e noventa e nove'})

print('PASSED ALL TESTS!')
