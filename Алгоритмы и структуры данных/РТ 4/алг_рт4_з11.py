import json

with open('data.json', 'r') as json_file:
    data = json.load(json_file)
    dict_data = dict()
    for i in data:
        if dict_data.get(i["id"]) is None:
            dict_data[i["id"]] = [i["name"]]
        else: 
            dict_data[i["id"]] = dict_data[i["id"]] + [i["name"]]

print(dict_data)