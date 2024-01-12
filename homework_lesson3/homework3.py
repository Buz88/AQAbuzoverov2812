import random

#Zadacha 1

min = random.randint(0,59)
if min >= 0 and min < 15:
    print(min, 'First quarter')
elif min > 15 and min < 30:
    print(min, 'Second quarter')
elif min > 30 and min < 45:
    print(min, 'Third quarter')
else:
    print(min, 'Fourth quarter')

#Zadacha 2
'''
birth_month = input('Enter your birth month: ')
if birth_month.isnumeric():
    birth_month = int(birth_month)
    if birth_month >= 1 and birth_month <= 2 or birth_month == 12:
        print('Зима - За вікном падав сніг.')
    elif birth_month >= 3 and birth_month <= 5:
        print('Весна - Все довкола розцвітало.')
    elif birth_month >= 6 and birth_month <= 8:
        print('Літо - Діти насолоджувались літніми канікулами.')
    elif birth_month >= 9 and birth_month <= 11:
        print('Осінь - Все довкола загоралось яскравими фарбами.')
else:
    print('Invalid input')

#Zadacha 3

number = random.randint(1,1000)
print(number)
number = str(number)
a = str(number[0])
b = str(number[1])
c = str(number[2])
suma = int(a) + int(b) + int(c)
number = int(number)
if number % 6 == 0 and suma % 3 == 0:
    print('Число х ділиться на 6')
else:
    print('Число х не ділиться на 6')

'''
#Zadacha 4


input_x = float(input('Введи значення Х: '))
input_y = float(input('Введи значення Y: '))
if input_x == 0 and input_y == 0:
        print('Точка лежить на початку координат')
elif input_x > 0 and input_y > 0:
        print('Точка лежить в першій чверті')
elif input_x > 0 and input_y < 0:
        print('Точка лежить в другій чверті')
elif input_x > 0 and input_y == 0:
        print('Точка лежить на осі Х справа ')
elif input_x < 0 and input_y > 0:
        print('Точка лежить в четвертій чверті')
elif input_x < 0 and input_y < 0:
        print('Точка лежить в третій чверті чверті')
elif input_x < 0 and input_y == 0:
        print('Точка лежить на осі Х зліва ')
elif input_x == 0 and input_y > 0:
        print('точка лежить на осі Y вгорі ')
elif input_x == 0 and input_y < 0:
        print('точка лежить на осі Y внизу')
else:
    print('Invalid input for point')



