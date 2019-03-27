UNIT = {'00': '', '01': 'um', '02': 'dois', '03': 'tres', '04': 'quatro',
        '05': 'cinco', '06': 'seis', '07': 'sete', '08': 'oito',
        '09': 'nove', '10': 'dez', '11': 'onze', '12': 'doze',
        '13': 'treze', '14': 'quatorze', '15': 'quinze', '16': 'dezesseis',
        '17': 'dezessete', '18': 'dezoito', '19': 'dezenove'}

TENS = {'0': '', '2': 'vinte', '3': 'trinta', '4': 'quarenta',
        '5': 'cinquenta', '6': 'sessenta', '7': 'setenta',
        '8': 'oitenta', '9': 'noventa'}

HUNDRED = {'0': '', '1': 'cento', '2': 'duzentos', '3': 'trezentos',
           '4': 'quatrocentos', '5': 'quinhentos', '6': 'seiscentos',
           '7': 'setecentos', '8': 'oitocentos', '9': 'novecentos'}

THOUSAND = {'00': '', '01': 'mil'}


def getUnit(number):
    if number['unit'] in UNIT:
        return UNIT[number['unit']]
    elif number['unit'][0] != '0' and number['unit'][1] == '0':
        return TENS[number['unit'][0]]
    else:
        return TENS[number['unit'][0]] + ' e ' + UNIT['0' + number['unit'][1]]


def getHundred(number):
    return HUNDRED[number['hundred']]


def getThousand(number):
    if number['thousand'] in THOUSAND:
        return THOUSAND[number['thousand']]
    elif number['thousand'] in UNIT:
        return UNIT[number['thousand']] + ' ' + 'mil'
    elif number['thousand'][1] == '0':
        return TENS[number['thousand'][0]] + ' ' + 'mil'
    else:
        return TENS[number['thousand'][0]] + ' e ' + UNIT['0' + number['thousand'][1]] + ' mil'


def writter(path):
    number = {}

    if '-' in path:
        number['sign'] = 'minus'
        path = path.zfill(6)
        path = path.split('-')[1]
    else:
        number['sign'] = 'plus'
        path = path.zfill(5)

    number['unit'] = path[3:5]
    number['hundred'] = path[2]
    number['thousand'] = path[0:2]

    unit = getUnit(number)
    hundred = getHundred(number)
    thousand = getThousand(number)

    result = {'extenso': ''}

    if unit == '' and hundred != '':
        if hundred == 'cento' and unit == '':
            result = {'extenso': 'cem'}
        else:
            result = {'extenso': hundred}
    elif hundred == '' and unit != '':
        result = {'extenso': unit}
    elif hundred == '' and unit == '':
        result = {'extenso': ''}
    else:
        result = {'extenso': getHundred(number) + ' e ' + getUnit(number)}

    if result['extenso'] == '' and thousand == '':
        result['extenso'] = 'zero'
    elif result['extenso'] == '' and thousand != '':
        result['extenso'] = thousand
    elif result['extenso'] != '' and thousand == '':
        pass
    elif hundred != '' and thousand != '':
        if result['extenso'].find('cento ') != -1:
            result['extenso'] = thousand + ' ' + result['extenso']
        else:
            result['extenso'] = thousand + ' e ' + result['extenso']
    else:
        result['extenso'] = thousand + ' e ' + result['extenso']

    if number['sign'] == 'minus' and result['extenso'] != 'zero':
        result['extenso'] = 'menos ' + result['extenso']

    return result
