def dollar(func):
    def inner(*args, **kwargs):
        header, footer = "$" * 20, "$" * 20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner
def star(func):
    def inner(*args, **kwargs):
        header, footer = "*" * 20, "*" * 20
        return f"{header}\n{func(*args, **kwargs)}\n{footer}"
    return inner

def add_footer_header(sign,quantity):
    def middle_decorator(func):
        def inner(*args, **kwargs):
            footer = sign*quantity
            header = sign*quantity
            return f"{header}\n{func(*args, **kwargs)}\n{footer}"
        return inner
    return middle_decorator


@add_footer_header('&',2)
@dollar
@star
def hi(msg):
    return "$$$\n***\n" +msg+ "\n***\n$$$"

print(hi("Hello World"))

#Декоратор, который выводит время выполнения функции
import datetime
def a_func(func):
    def inner(*args, **kwargs):
        a = datetime.datetime.now()
        result = func(*args, **kwargs)
        b = datetime.datetime.now()
        print("diff = ", b-a)
        return result
    return inner

@a_func
def counter_func(num):
    total = sum([x for x in range(0, num**2)])
    return total

print(counter_func(5000))