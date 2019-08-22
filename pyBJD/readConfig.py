import json

with open('../name.json') as name:
    data = json.load(name)
print(data)
