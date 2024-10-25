import json

data = {
    'name': "thoth",
    "id":'python',
    "languages": ["English", "Spanish"]
}

with open("data.json",'w') as file:
    json.dump(data, file, indent=4)

with open('data.json','r') as file:
    data = json.load(file)

if 'id' in data:
    del data['id']
print(data)