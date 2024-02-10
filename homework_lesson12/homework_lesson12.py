
import time
import datetime
'''Реалізуйте функцію, яка додає або віднімає від заданої дати певну кількість днів.
Приймає на вхід будь-яку дату та час (datetime),
а також значення днів(int), і знак(True або False, які репрезентують + і -).
Повертає datetime. В цій задачі скористайтесь datetime.timedelta
def input_dates():
    while True:
        try:
            first_date = input("Введіть першу дату у форматі YYYY-MM-DD: ")
            second_date = int(input("Введіть кількість днів: "))
            first_date_upd = datetime.datetime.strptime(first_date, "%Y-%m-%d")
            second_date_upd = datetime.timedelta(days=second_date)
            return first_date_upd, second_date_upd
        except ValueError:
            print('invalid input, please try again')

first_date, second_date = input_dates()
difference = first_date+second_date
d3=datetime.datetime.strftime(difference, "%Y-%m-%d")

if difference > first_date:
    print(f'Ось твоя дата від {datetime.datetime.strftime(first_date, "%Y-%m-%d")} після {second_date} складає {datetime.datetime.strftime(difference, "%Y-%m-%d")} True')
else:
    print(f'Ось твоя дата від {datetime.datetime.strftime(first_date, "%Y-%m-%d")} після {second_date} складає {datetime.datetime.strftime(difference, "%Y-%m-%d")} False')

Реалізуйте функцію, яка вираховує ваш точний вік(не обов'язково вказувати свої данні),
вираховуючі різницю між наданим значенням і значенням datetime.now(). Приймає дату та час(datetime),
повертає три значення: datetime.timedelta, datetime.timestamp прожитого життя і строкове значення
часу народження в форматі (рік(останні два числа, день, місяць, години, хвилини,секунди, am/pm в 12
годинному форматі). Виведіть результат в консоль


birth_date_str = input("Введіть свою дату народження у форматі YYYY-MM-DD HH:MM:SS: ")
birth_datetime = datetime.datetime.strptime(birth_date_str, "%Y-%m-%d %H:%M:%S")
birth_time_str = birth_datetime.strftime("%y-%m-%d %I:%M:%S %p")
age_timedelta = datetime.datetime.now() - birth_datetime
age_seconds = age_timedelta.total_seconds()
age_timestamp = birth_datetime.timestamp()

print("Ваш вік:", age_timedelta)
print("Прожите життя у секундах:", age_timestamp)
print("Час народження:", birth_time_str)

Створіть обробку одного будь-якого exception,
який не використався як приклад на занятті, 
додайте обробку решти ексепшенів за допомогою Exception.
Виведіть результат в консоль

def my_function(value):
    try:
        value = int(value)
    except ValueError as e:
        print("Помилка конвертації:", e)
    except Exception as e:
        print("Виникла помилка:", e)
    else:
        print("Значення успішно конвертовано:", value)
    finally:
        print("Завершення програми")


my_function('sdadasdfasdfa')
'''