# асоціативний масив, простіше це послідовність асоціативна у нас замість індексів використовуються ключі схоже на сет але в середині ключ значення
perfect_dict = {'one': 1, 'two': 2, 'banana': 'yes', 14: 6, False: [1, 2, 3, {'one': 1, 'two': 2, 'banana': 'yes'}]}
lil_bit_less_perfect_dict = {
    1: 2,
    'three': 3,
}
'''
perfect_dict[14] = 15
print(perfect_dict[14])
print(lil_bit_less_perfect_dict)
print(len(perfect_dict))
print(perfect_dict['banana'].islower())
print(perfect_dict['one'] > perfect_dict['two'])
del perfect_dict[14]
print(perfect_dict)
print('one' in perfect_dict)
lil_bit_less_perfect_dict.clear()
print(lil_bit_less_perfect_dict)
ugly_dict = perfect_dict.copy()
print(ugly_dict)
dict_keys = perfect_dict.fromkeys(ugly_dict)
print(dict_keys)
a = None
print(a)
print(type(a))
a = 1
print(a)
print(type(a))
print(type(None))
print(type(''))
print('' == None)
print(perfect_dict.get('one'))
keys_list = list(perfect_dict.keys())
print(perfect_dict.values())
keys_list.pop()
print(keys_list)
'''
for key, value in perfect_dict.items():
    print(key, value)
a = perfect_dict.pop('one')
print(a)
print(perfect_dict)
b = perfect_dict.popitem()
print(b)
new_value = 100
new_value1 = 1000
new_key = 'hundred'
new_key1 = 'thousand'
perfect_dict[new_key] = new_value
print(perfect_dict)
new_dict = dict()
counter = 0
for key, value in perfect_dict.items():
    if counter == 1:
        new_dict[new_key1] = new_value1
    new_dict[key] = value
    counter += 1
print(new_dict)
