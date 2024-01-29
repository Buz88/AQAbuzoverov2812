'''Напишіть програму яка перевіряє чи стрічка містить
лише великі і малі літери, числа та нижнє підкреслення.
Напишіть програму, що видаляє область дужок в стрічці
["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
example
github
stackoverflow

Напишіть програму, що. вставляє пробіл перед великою літерою'''
import re
stringa1 = 'aZ54_%^&*()-_=+,./0123456789'
pattern = '[A-Za-z0-9_]'
test1 = re.findall(pattern, stringa1)
print(test1)

'''
home_str1 = 'example (.com)'
home_str2 = 'github (.com)'
home_str3 = 'stackoverflow (.com)'
pattern = r'\([^)]*\)'
match1 = re.sub(pattern, '\n', home_str1)
match2 = re.sub(pattern, '\n', home_str2)
match3 = re.sub(pattern, '\n', home_str3)
print(match1, match2, match3)

string1 = 'kfjAjfksQjfdkAjkdsfD'
pattern1 = r'([a-z])([A-Z])'
test = re.sub(pattern1, r'\1 \2', string1)
print(test)
'''