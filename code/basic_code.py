#cryptodisplay

import requests

#FIND CURRENT BTC VALUE
response_BTC = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response_BTC.json()
#print(data["bpi"]) TEST
print ("BTC Value: ")
print(data["bpi"]["GBP"]["rate"])

#FIND CURRENT ETH VALUE
response_ETH = requests.get('https://api.coinbase.com/v2/prices/ETH-GBP/spot')
data2 = response_ETH.json()
#print(data2) TEST
print ("ETH Value: ")
print(data2["data"]["amount"])
print ("")


