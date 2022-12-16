import requests as re

# pip install requests

# response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/")
# response = re.get("http://api.nbp.pl/api/exchangerates/rates/A/USD/today/")
response = re.get("http://api.nbp.pl/api/exchangerates/tables/A/")
# GET, POST, PUT, DELETE - REST API
print(response)
# 200 - OK
table = response.json()
print(table)
print(table[0]['rates'][0]['mid'])
# print(table['table'])
# print(table['currency'])
# print(table['code'])
# print(table['rates'])
# print(table['rates'][0])
# print(table['rates'][0]['mid'])
# print(table['rates'][0]['effectiveDate'])
# print(table['rates'][0]['no'])
14:00 