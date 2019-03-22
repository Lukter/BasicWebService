import requests
import json

response = requests.get('http://localhost:5000/1')
assert(response.json() == {'extenso': 1})

response = requests.get('http://localhost:5000/0')
assert(response.json() == {'extenso': 0})

response = requests.get('http://localhost:5000/1.1')
assert(response.json() == {'ERRO': '1.1'})

response = requests.get('http://localhost:5000/1,1')
assert(response.json() == {'ERRO': '1,1'})

response = requests.get('http://localhost:5000/99998')
assert(response.json() == {'extenso': 99998})

response = requests.get('http://localhost:5000/99999')
assert(response.json() == {'extenso': 99999})

response = requests.get('http://localhost:5000/-1')
assert(response.json() == {'extenso': -1})

response = requests.get('http://localhost:5000/-1.1')
assert(response.json() == {'ERRO': '-1.1'})

response = requests.get('http://localhost:5000/-1,1')
assert(response.json() == {'ERRO': '-1,1'})

response = requests.get('http://localhost:5000/-99998')
assert(response.json() == {'extenso': -99998})

response = requests.get('http://localhost:5000/-99999')
assert(response.json() == {'extenso': -99999})

response = requests.get('http://localhost:5000/9999999999999')
assert(response.json() == {'ERRO': '9999999999999'})

response = requests.get('http://localhost:5000/-9999999999999')
assert(response.json() == {'ERRO': '-9999999999999'})

response = requests.get('http://localhost:5000/a')
assert(response.json() == {'ERRO': 'a'})

response = requests.get('http://localhost:5000/a1a1a1a1a1')
assert(response.json() == {'ERRO': 'a1a1a1a1a1'})

response = requests.get('http://localhost:5000/-a')
assert(response.json() == {'ERRO': '-a'})

response = requests.get('http://localhost:5000/-a1a1a1a1a1')
assert(response.json() == {'ERRO': '-a1a1a1a1a1'})
