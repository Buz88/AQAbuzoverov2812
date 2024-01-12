first_list = [1, 6, 8, 4, 6, 3, 5, 2]
print(sorted(first_list, reverse=True))
print(first_list[4:])
print(first_list[:4])
second_list = first_list[:4]
print(second_list)

print(first_list[2:5])
first_list.extend(second_list)
print(first_list)
third_list = []
for element in first_list:
    third_list.append(element * 2)
print(third_list)
'''
a = [1,2,3,4]
b = a
a.append(5)
b.append(6)
print(a)
print(b)
c = a.copy()
c.pop()
print(a)
print(c)

a = [1,2]
b = [3,4]
c = a + b
a.pop()
print(f'c:{c}')
a.extend(b)
b.pop()
print(f'c:{c}')
d = list(a)
print(f'd:{d}')
a.pop()
print(f'd:{d}')
print(id(a))
print(id(d))

first_list = [1, 6, 8, 6, 6, 3, 5, 2]
print(first_list.count(6))

print(first_list.reverse())

first_tuple = (4,5,6,7,8)
print(first_tuple[0])
elements_list = []
for element in first_list:
    if element > 5:
        elements_list.append(element)
print(elements_list)
counter = 0
while counter<10:
    print('Help me, Im stuck in the infinite loop')
    counter+=1

for element in 'Hello world':
    if element == 'o':
        continue
    print(element)
while counter < 30:
    counter += 1
    if counter % 2 == 1:
        print('im about to break')
        break
    print(counter)

for i in 'Hello world':
    if i == 'o':
        print(f'this string have {i} letter, Im about to die')
        break
    else:
        print(i)
else:
    print('this string have not any A letters')

'''

entered = 0

while True:
    new_entered = (input('Enter a number: '))
    if new_entered == 'sum':
        print(entered)
        break
    elif new_entered.startswith('-') and new_entered[1:].isnumeric() or new_entered.isnumeric():
        entered += int(new_entered)
    else:
        print('Not a valid number')