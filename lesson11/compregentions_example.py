'''some_list = [1,2,3,4,5,6,7,8,9]
new_list =[]

for i in some_list:
    if i>3:
        new_list.append(i)

print(new_list)

new_list2 = [i for i in some_list if i > 3]
print(new_list2)

new_list = [item**2 for item in range(10000000)]
print(new_list)

names = ['John', 'Smithana', 'Alexis', 'Anna', 'Smithana', 'Corolla']
new_dict={index:name for index, name in enumerate(names)}
print(new_dict)
for key, value in new_dict.items():
    print(key, value)

list_to_oreder = [1,2,3,4,5,22,22,100,100,120,32465,123,212,231]
new_set = {item for item in list_to_oreder if item>5}
print(new_set)
new_set2 =set(list_to_oreder)
print(new_set2)


new_gen = (item for item in range(10000))
print(new_gen)
for i in new_gen:
    print(i)
'''

new_gen = (*(item for item in range(100000000)),)
print(new_gen)
#*arg = rozpakowka pochitat
#**kwargs = rozpakowka pochitat