import random
# Zadacha_1 Дано два списки чисел.
# Знайдіть всі числа, що зустрічаються як в першому, так і другому списках, і надрукуйте їх у порядку зростання.
'''
def find_common_numbers(first, second):
    # Використовуємо set для ефективної перевірки наявності елементів
    list1 = set(first.split())
    list2 = set(second.split())
    find = list1.intersection(list2)
    sort = sorted(list(find))
    print("Спільні числа у порядку зростання:", sort)


mylist1 = input("Введіть свої числа, для першого списку:")
mylist2 = input("Введіть свої числа, для другого списку:")

find_common_numbers(mylist1, mylist2)
'''

# Zadacha_2
# Створіть словник із даними про студентів: ключі - імена студентів,
# значення - бали для кожного. Програма повинна визначити середній бал
# і вивести імена студентів, чий бал вище середнього.

students_dir1 ={'Alice': 85,'Bob': 92,'Charlie': 78,'David': 95,'Eva': 88}
students_dir = {'Іван':85, 'Марія':92, 'Петро':78, 'Олена':88, 'Анна':95}

def students():
    for student in students_dir:
        print(student, students_dir[student])
    average_score = sum(students_dir.values()) / len(students_dir)
    print(f"Середній бал студентів: {average_score}")
    above_average_students = [name for name, score in students_dir.items() if score > average_score]
    print("Студенти з балами вище середнього:")
    for student in above_average_students:
        print(f"{student}: {students_dir[student]} балів")

a = students()
print(a)



'''

# 3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba'].
# напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат.
# для випадковості значень скористайтесь модулем random. приклад згенерованого словника:
#
# {'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}

names = ['Robin', 'Liza', 'Kevin', 'George', 'Daniel', 'Williams','Ivan', 'Oleksandr']
surnames = ['Djoconda','Lop', 'John', 'Francisco', 'Edward', 'Gordon', 'Wellington']
locations = ['San Francisco', 'Kosta Rica', 'Florence', 'China', 'USA', 'Ukraine', 'Miami']

def generate_random_person():
    random_name = random.choice(names)
    random_surname = random.choice(surnames)
    random_location = random.choice(locations)

    person = {'name': random_name, 'surname': random_surname, 'location': random_location}
    return person

person = generate_random_person()
print(person)
'''