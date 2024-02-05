import json

'''
Python -> JSON
dict -> object {}
list, tuple -> array []
str -> string
int, float -> number
bool(True, False) -> boolean(true, false)
None -> null
'''

data = {
    'name': 'Alejandro',
    'age': 60,
    'songs': ['music1', 'music2', 'music3', 'music4'],
    'alive': True,
    'minuses': None,
    'base':{'base1':{'base2':{'unique_value':'12321'}}}
}
json_str = ''
with open('alejandro.json', 'w') as writer:
    json.dump(data, writer, indent=4)  # 4 - ce skiki probiliv 4=tab
    json_str = json.dumps(data, indent=4)
    print(json_str)

'''
object -> dict
array -> list
string -> str
number -> int,float
true, false -> True, False
null -> None
'''

data_outside_scope = {}
with open('alejandro.json', 'r') as reader:
    data_outside_scope = json.load(reader)
    print(data_outside_scope)
    print(type(data_outside_scope))

data1 = json.dumps(data_outside_scope)
data1 = data1.replace('unique_value', 'unique_value1',2)
data2 = json.loads(data1)
with open('modified_alejandro.json', 'w') as writer:
    json.dump(data2, writer, indent=4)



data1 = json.loads(json_str)
print(data1['songs'])
print(type(data1['songs']))