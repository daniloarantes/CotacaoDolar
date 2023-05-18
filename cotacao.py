from os import system
import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()

preco = float(cotacao['USD']['bid'])

print("Moeda: " + cotacao['USD']['name'])
print("Data: " + cotacao['USD']['create_date'])
print("Valor Atual: R$ " + cotacao['USD']['bid'])