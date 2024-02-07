#iterator - object, zbilshue lichilnik, stop iteraciy, zberigae vsy poslidovnist
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers_iterator = iter(numbers)
print(numbers_iterator)
#for number in numbers_iterator:
   # print(number)
print(next(numbers_iterator))
print(next(numbers_iterator))

a = []
def my_generator():
    counter = 0
    while True:
        yield counter **2
        counter +=1

generator = my_generator()
print(my_generator())
print(next(generator))
a.append(next(generator))
print(next(generator))
a.append(next(generator))
print(next(generator))
a.append(next(generator))
print(next(generator))
a.append(next(generator))
print(a)
'''
def my_gen():
    counter = 0
    while True:
        yield counter **2
        counter +=1

gen = my_gen()
for i in gen:
    print(i)

