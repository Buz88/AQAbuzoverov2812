'''
Створіть декоратор, який виводить в консоль ім'я функції, яку було викликано. Наприклад, створіть пару функцій для арифметичних операцій додавання і множення.
При виклику цих функцій має повертатись результат операції і виводиться в консоль ім'я функції,
яку було викликано.

def decor(func):
    def inner(*args, **kwargs):
        print(f'Name of the function: {func.__name__}')
        return func(*args, **kwargs)
    return inner


@decor
def sum(a,b):
    return a+b
@decor
def minus(a,b):
    return a-b
@decor
def multiplication(a,b):
    return a*b
@decor
def division(a,b):
    return a/b

print(sum(1,2))
print(minus(1,2))
print(multiplication(1,2))
print(division(1,5))

Створіть за допомогою list comprehension список, в якому буде 100 елементів,
і кожен із яких буде в границях від 1 до 10(для цього можна скористатись функцією
randint із модуля random). Порахуйте кількість кожного елемента і виведіть в консоль
'''

import random
my_list = [random.randint(1,10) for i in range(100)]
print(len(my_list))
print(my_list)
