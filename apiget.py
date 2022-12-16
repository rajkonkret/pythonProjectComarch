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
# 200: Everything went okay, and the result has been returned (if any).
# 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
# 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
# 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
# 403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
# 404: The resource you tried to access wasn’t found on the server.
# 503: The server is not ready to handle the request.