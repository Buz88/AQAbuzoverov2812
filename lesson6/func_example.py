# функція іменований блок коду, що вирішує задачі, ваша функція повинна вирішувати по можливості одну задачу
'''def name_greeter():
    your_name = input("What is your name? ")
    print(f'Hello, {your_name}')


name_greeter()
name_greeter()
name_greeter()


def im_a_new_cool_func(value, value2):
    print(value ** value2)


im_a_new_cool_func(value=6, value2=3)


def print_full_name(first_name, last_name):
    print(f'Hello, {first_name} {last_name}')
print_full_name('oleh', None)
print_full_name(first_name='oleh', last_name='versh')

def my_favorite_language(name, language='Python'):
    print(f'Hello my name is {name} and my favorite language is, {language}')

my_favorite_language('soso', language='Java')
my_favorite_language('Mykyta', 0)


def mr_sum_two_numbers(first_number, second_number)->int:
    return first_number + second_number

new_value = mr_sum_two_numbers(5,6)
print(new_value)

def make_pizza(*ingridients)->str:
    for ingr in ingridients:
        print(f'{ingr}is a {ingridients.index(ingr)} number ingridienses in pizza')

make_pizza('pepperoni')
make_pizza('cheese', 'cheese', 'cheese', 'cheese')
make_pizza('pineapple', 'curse')



def dogs(**dog_info) -> dict:
    for key, value in dog_info.items():
        print(f'{key}: {value}')


dogs(first_name='Patron', required_amount=100000, cooler_then='iphon')
'''


def sum_and_diff(first, second):
    return first + second, first - second


if __name__ == '__main__':  # щоб запускалося тіки те шо треба
    sum_result, diff_result = sum_and_diff(5, 10)
    print(sum_result)
    print(diff_result)
    sum_and_diff_result = sum_and_diff(20, 10)
    print(sum_and_diff_result)
    print(sum_and_diff_result[1:])
