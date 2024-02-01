# Напишіть програму на Python для знаходження
# перетину двох заданих масивів за допомогою лямбда.

# Напишіть програму на Python, щоб
# перевірити, чи є заданий рядок числом, за допомогою лямбда

# Напишіть програму на Python, щоб знайти
# список із максимальною та мінімальною довжиною за допомогою лямбда.

# Zadacha 1
'''
find_intersection = lambda a, b: list(filter(lambda x: x in a, b))

a = [1,2,3,4,5,6,7,8,9,10]
b = [22,3,44,5,8888,9345,'sad']

intersection = list(find_intersection(a, b))
print(intersection)
'''
# Zadacha 2
number = lambda s: s.isnumeric() if s.isnumeric() else (s.replace('.', '', 1).isdigit() if '.' in s else False)

input_1 = input('Enter a number: ')
result = number(input_1)

if result == True:
    print(f'{input_1} is a number')
else:
    print(f'{input_1} is not a number')

'''
# Zadacha 3
lists = [[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9],[1,2,3],[1,2],[2]]
find_min = lambda list: (min(list, key=lambda x: len(x)))
find_max = lambda list: (max(list, key=lambda x: len(x)))

print(f'Мінімальне значення {find_min(lists)} та максимальне значення твого листу: {find_max(lists)}')
print(f'Мінімальне значення {len(find_min(lists))} та максимальне значення твого листу: {len(find_max(lists))}')
'''


