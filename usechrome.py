import json

with open("config.json", "r") as jsonFile:
    data = json.load(jsonFile)
tmp = data["browser"]
data['browser'] = 'chrome'
with open("config.json", "w") as jsonFile:
    json.dump(data, jsonFile)
