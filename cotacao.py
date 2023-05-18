from os import system
import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()

preco = float(cotacao['USD']['bid'])

print(f"Moeda: {cotacao['USD']['name']}")
print(f"Data: {cotacao['USD']['create_date']}")
print(f"Valor Atual: R$ {cotacao['USD']['bid']}")