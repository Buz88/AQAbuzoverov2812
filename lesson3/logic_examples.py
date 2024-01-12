new_value = True
false_value = False
print(int(new_value))
print(int(false_value))
print(bool(1))
print(bool(0))
a = 0
b = bool(a)
print(b)
new_sting = 'fish'
empty_string =''
print(bool(new_sting))
print(bool(empty_string))
'''
<
>
<=
>=
==
!=
'''
a1 = 100
b1 = 200
print(a1>=b1)
print(a1<=b1)
print(a1==b1)
print(a1!=b1)

'''int_value_to_read = input('Hey dude print input immideatly')
if int_value_to_read.isdigit():
    print(int_value_to_read)
else:
    print('Invalid input')

input_value = int(input('Hey dude, tell me your number'))
if input_value > 0:
    print(input_value)
else:
    print(input_value*(-1))

int_value_to_read = int(input('Hey dude print smthing immideatly'))
if int_value_to_read >= 9:
    print('Your number have 2 or more digits')
else:
    print('Your number have 1 digits')

# or and not
int_value_to_read = int(input('Hey dude print int input immideatly'))
if int_value_to_read > 30 or int_value_to_read < 20:
    print('Ha your number between 10 and 20, probably')

if int_value_to_read > 200 and int_value_to_read % 20 == 0:
    print('oh no')

if not int_value_to_read:
    print('hell yea')


str_input = input('Hey dude, tell me')

if str_input.startswith('Hello'):
    print('Hello there')
elif str_input.isdigit() and not str_input.startswith('2'):
    print('I see you mr robot')
elif str_input.startswith('2'):
    print('Second')
else:
    print('you typed invalid character')

eyes = int(input('How many eyes?'))
legs = int(input('How many legs?'))
if eyes >= 8:
    if legs == 8:
        print('Spider')
    elif legs == 6:
        print('Cockroach')
    else:
        print('undefined creature')
else:
    if eyes == 2 and legs == 4:
        print('definitely a cat')
    else:
        print('horror beyond our comprehension')
'''
cool_fruits = 'watermelon'
fruits = ['apple', 'banana', cool_fruits, 'watermelon']
print(fruits)
print(type(fruits))
print(id(fruits))
print(len(fruits))
print(fruits[2])
print(fruits.index('watermelon', 3))
fruits.append('lemon')
print(fruits)
fruits.pop(2)
print(fruits)
del fruits[0]
print(fruits)
fruits.clear()
print(fruits)



