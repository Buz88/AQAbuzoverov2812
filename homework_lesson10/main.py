from package_1 import my_sum, my_divide
import re
import csv
'''
print(my_sum(4,5))
print(my_divide(5,4))

2. Написати функцію, яка отримує у вигляді параметра ім'я файлу 
назви інтернет доменів (domains.txt) та повертає їх у вигляді списку 
рядків (назви повертати без крапки).

lines = []
with open('domains.txt') as d:
    domains = [line.strip().replace('.', '') for line in d.readlines()]
    lines.append(domains)
    print(lines)


3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і 
повертає список усіх прізвищ з нього. Кожен рядок файлу містить номер, 
прізвище, країну. Файл створити власноруч і записати туди дані


surnames=[]
with open('names.txt', 'r') as n:
    for line in n:
        data = line.strip().split(' ')
        if len(data) >= 2:
            surname = data[1]
            surnames.append(surname)
print(surnames)


4. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt)
і повертає список словників виду {"date": date} у яких date - це дата з рядка 
(якщо є),Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]


my_dict = {}
dates_list = []
with open('authors.txt', 'r') as a:
    for line in a:
        date_pattern = re.search(r'\b\d{1,2}(st|nd|rd|th) [A-Za-z]+ \d{4}\b', line)
        if date_pattern:
            dates_list.append({"date": date_pattern.group(0)})
            my_dict = {"date": date_pattern.group(0)}
        print(my_dict)
        
        
'''

'''
5.Створіть функцію, яка читає файл csv. 
Вона приймає назву файлу(str), повертає список рядків(list). 
Також створіть функцію, яка записує в файл данні. 
Вона приймає назву файлу(str), список рядків(list), які треба записать в файл.
Нічого не повертає. 
Тепер за допомогою створених функцій спочатку створіть файл(3 рядків достатньо),
потім прочитайте той-же файл, записавши рядки в змінну, потім додайте два 
рядки в змінну, і після цього запишіть ваші зміни в інший файл.
'''

data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', '25', 'New York'],
    ['Alice', '30', 'Los Angeles']]

with open('file.cvs', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)

rows = []
with open('file.cvs', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        rows.append(row)

with open('file.cvs', 'r') as file:
    reader = csv.reader(file)
    print("Початкові дані:")
    for row in reader:
        print(row)

new_rows = [
    ['Bob', '22', 'Chicago'],
    ['Eva', '28', 'San Francisco']]

with open('updated_file.csv', 'w', newline='') as updated_file:
    writer = csv.writer(updated_file)
    writer.writerows(data_to_write)
    writer.writerows(new_rows)

with open('updated_file.csv', 'r') as updated_file:
    reader = csv.reader(updated_file)
    print("Початкові дані:")
    for row in reader:
        print(row)




