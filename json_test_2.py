import json

with open('dane_json.json', 'r') as f:
    data = json.load(f)

print(data)
print(data['members'])
print(data['members'][0])
print(data['members'][0]['name'])
print(data['members'][0]['age'])
print(data['members'][0]['powers'])
print(data['members'][0]['powers'][0])

print(data['members'])
print(data['members'][2])
print(data['members'][2]['name'])
print(data['members'][2]['age'])
print(data['members'][2]['powers'])
print(data['members'][2]['powers'][0])

for i in data['members']:
    print(i)
    print(i['name'], i['age'])
    print(i['age'])
    print(i['powers'])
