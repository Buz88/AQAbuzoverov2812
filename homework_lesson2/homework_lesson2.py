import math

#Завдання 1


first_name = 'oleksandr'
last_name = 'buzovierov'
print(first_name +' ' + last_name)
print(first_name.capitalize() + ' ' + last_name.capitalize())
print(first_name.upper() + ' ' + last_name.upper())
print(first_name.lower() + ' ' + last_name.lower())
#1.3
first_name1 = '\t' +'    oleksandr     ' + '\n'
print(first_name1.strip().capitalize())


#Завдання 2


print("Будь-ласка введіть радіус кола...")
R = int(input())
L = 2 * math.pi * R
S = math.pi * R ** 2
print(f"Довжина кола дорівнює {L}")
print(f"Площа кола дорівнює {S}")


#Завдання 3


dollar_course = 39.2
convert = 1000/dollar_course
conv_round = round(convert,2)
print('Поточний курс складає: '+ str(conv_round))
