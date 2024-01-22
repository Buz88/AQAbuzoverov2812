'''from func_example import sum_and_diff

a,b = sum_and_diff(500,100)# значення за замовченням теж вказуємо
print(a)
print(b)
print(a, b)
'''

# zadacha 1
# Чи задане число потрапляє в заданий діапазон фром і ту
'''
def check_number(num1=0, num2=100):
    entered = int(input('Enter a number: '))
    if entered > num1 and entered < num2:
        print(f'The entered {entered} in between {num1} and {num2}')
        return True
    else:
        print('Wrong number')
        return False


result = check_number()
print(result)
'''


# zadacha 2
# напишіть функцію яка отримує стрічку конструкцію та цикл фор якщо невалідні символи видалити строку

#ZARABOTALO!!!!!!!!!!!
def check_string(*symbols):
    string = input('Enter something: ')
    for symbol in string:
        if symbol in symbols:
            string = string.replace(symbol, '')
    return string


s = check_string('!', '@', '#', '$', '%', '^', '&', '*', '(', '<', ')', '_', '(', '+', '=')
print(s)
