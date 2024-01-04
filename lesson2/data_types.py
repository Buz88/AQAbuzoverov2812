import math
import random

# typs dannih zminyvani i nezminyvani

a = 1  # int
b = 1
print(a)
print(id(b))
print(id(a))
# однакові ід бо маленькі обєкти
print(type(a))

c = 2.5  # float
d = True  # bool
the_name_of_the_person = 'text'  # str

print(type(c))
print(type(d))
print(type(the_name_of_the_person))

# в назвах заборонені пробіли
# не можна використовувати зарезервовані слова https://letpy.com/handbook/keywords/

second_int = 2
print(a + second_int)

third_int = a + second_int
print(third_int)
print(second_int - 1)
print(second_int * 4)
print(second_int / 2)
print(3 ** 3)
print(2 + 3 * 4)
print((2 + 3) * 4)
print(8 // 4)  # без залишка
print(9 % 4)  # залишок від ділення
print(2 + 2.5)

'''
1. **
2. *, /, //, %
3. +, -
'''

new_value = 2 + 2.5
print(type(new_value))

small_number = 0.1
smaller_number = 0.000000001
print(0.2 + 0.1)
first_float = 2.345678905
print(round(first_float, 4))
print(dir(math))
print(math.pi)
print(math.cos(0))
print(dir(random))
print(random.randint(20,30))
print(random.randrange(15))                         # він бере від 0 завжди навідміну від randint
print(random.choice(['black', 'white', 'grey']))    # витягає зі списку одне рандомне значення

newqw_string = 'asdfasdfa'
new_string = "I'm i don't know\" dude"
another_new_string = 'this is called "wednesday"'

print(dir('a'))
message = "i'm a sMall message"
print(message.title())
print(message.capitalize())
print(message.upper())
print(message.lower())
first_name = 'Oleh'
last_name = 'Vershinin'
full_name = '\t' + first_name + ' ' + last_name
print(full_name)
print('students:\nOlha \nVolodymyr')
print('python            '.rstrip())
print('            Python'.lstrip())
print('      Python     '. strip())
py_string_example = 'python is very bad bad bad language'
print(py_string_example.replace('bad','good', 2))
print('bad' in py_string_example)
print('good' in py_string_example)
print(type(py_string_example))
print(py_string_example.islower())
print(py_string_example.isupper())
print(py_string_example.startswith('python'))
print(py_string_example.endswith('lang'))
print(py_string_example.isalpha())
one = "1"
print(one.isdigit())
special_symbols = '\n\t     '
print(special_symbols.isspace())
print(special_symbols.isprintable())
print(py_string_example.islower(), py_string_example.isspace())
print(py_string_example.capitalize().startswith('Python'))
print(py_string_example.count('bad'))
print(py_string_example.index('bad'))
print(py_string_example.find('bad'))
print(len(py_string_example))
splitted_string = py_string_example.split('very', 1)
print(splitted_string)
lines_example = 'a\n b\nc'
print(lines_example.splitlines())
print(py_string_example[20])
print(py_string_example[10:20])
food = 'Pizza'
cost = 150
str_cost = str(cost)
print('your'+food+'cost'+str_cost)
print('Your % costs % hryvnias'% (cost, cost))

print('thanks for this {}, here`s your {}'.format(food, cost))
print(f'Happilly, I want home with my {food}, and without my {cost} hryvnas')