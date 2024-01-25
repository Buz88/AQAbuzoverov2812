import math
from functools import reduce

def func_name():
    pass


# lambda arg1, arg2 ....argn:expression

double = lambda x: x * 2
print(double(2))
print(double(3))
print(double(4))


def fun_double(x):
    return x * 2


def to_cube(x):
    return x * x * x


lambda_to_cube = lambda x: x * x * x

print(to_cube(3))
print(lambda_to_cube(3))

lambda_multiple_three = lambda a, b, c: a * b * c
print(lambda_multiple_three(2, 3, 4))

sqrt_x = lambda x: math.sqrt(x)
print(sqrt_x(9))

lambda_list = [
    lambda x: x * 2,
    lambda x: x * 3,
    lambda x: x * 4
]
print(lambda_list[0](2))
for element in lambda_list:
    print(element(6))

lambda_tuple = (
    lambda x: x * x,
    lambda x: x * x * x,
    lambda x: x * x * x * x
)

for element in lambda_tuple:
    print(element(10))

areas_dictionary = {
    'circle': lambda radius: math.pi * radius ** 2,
    'rectangle': lambda a, b: a * b,
    'square': lambda a: a * a
}

print(areas_dictionary['square'](4))
print(areas_dictionary['rectangle'](12, 29))
print(round(areas_dictionary['circle'](6), 3))  # round зробив сам чисто по прекалу

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x % 2 == 0, list_a))
print(filtered_list)

filtered_odd_list = list(filter(lambda x: x % 2 != 0, list_a))
print(filtered_odd_list)

double_list = list(map(lambda x: x * 2, list_a))
print(double_list)

double_list_but_in_differnt_way = list(map(fun_double, list_a))
print(double_list_but_in_differnt_way)
print(type(fun_double))

triple_lists = list(map(lambda a, b, c: a + b + c, list_a, list_a, list_a))
print(triple_lists)

list_of_letters = ['a', 'b', 'c', 'd', 'e', 2]


sum_body = reduce(lambda x, y: x + y, list_a)  # попарно виконує функцію додавання послідовно
sum_body_2 = reduce(lambda x, y: x + y if type(y) == str else x + str(y), list_of_letters)
print(sum_body)
print(sum_body_2)
list_b = [90, 50, 40, 20, 30, 60]
min_el = reduce(lambda a, b: a if (a < b) else b, list_b)
min_el_but_different_way = reduce(min, list_b)
print(min_el)
print(min_el_but_different_way)

max_number = lambda x, y: x if x > y else y
print(max_number(14, 29))

list_c = [[15, 9, 12], [4, 1, 7], [20, 10]]
# sorted_list = lambda x: (sorted(x, key=lambda x: x[0])) #lambda x:(sorted(el) for el in x)
# print(list(sorted_list(list_c)))
# Об'єднати всі елементи в один плоский список
flat_list = [num for sublist in list_c for num in sublist]
print(flat_list)
# Відсортувати плоский список
flat_list.sort()
# Розбити відсортований плоский список назад на внутрішні списки
sorted_list_c = [flat_list[i:i + len(list_c[0])] for i in range(0, len(flat_list), len(list_c[0]))]
print("Відсортований список за всіма цифрами:")
print(sorted_list_c)
