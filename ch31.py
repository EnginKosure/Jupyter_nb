# QUESTION:
# Write a Python code to get current Bitcoin price from Binance exchange,
# and convert Json data to Python Object, and print this Python Object.
# To get current Bitcoin price use below API code. This code returns a JSON data.
# import requests
# import json
# response = requests.get(
#     'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
# btc = response.json()
# print(btc)  # {'symbol': 'BTCUSDT', 'price': '11662.70000000'}
# print(f"\n{btc['symbol']} price is ${int(float(btc['price']))}")
# # BTCUSDT price is $11,662

import requests
import json
api_url = 'https://api.binance.com/api/v3/ticker/price?symbol='
coin = input(
    "Which coin do you buy enter 'e' for etherium, 'b' for Bitcoin  : ")
coin = 'ETHUSDT' if coin == 'e' else 'BTCUSDT'
count_of_coin = int(input(f"How many {coin} will you buy : "))
result = requests.get(api_url+coin)
result = result.json()
# result = json.loads(result.text)  Bir üst satırdaki komut yerine buda yazılıyor.
print(result, "\n")
print(f"{result['symbol']} price is =  ${round(float(result['price']),2):,}\n")
print(
    f"{count_of_coin} {coin} price is = ${round((float(result['price'])*count_of_coin),2):,}\n")
