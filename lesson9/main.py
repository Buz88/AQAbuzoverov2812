# import lesson9.arithmetic as module
# from lesson9.arithmetic1 import my_sum, my_difference
# from lesson9.arithmetic import *
# from lesson9 import arithmetic1
# from lesson9.arithmetic1 import my_sum as sum1
# from lesson9.arithmetic2 import my_sum as sum2


bubba_salary = 200
uga_buga_salary = 100

# print(module.my_sum(bubba_salary, uga_buga_salary))
# print(my_sum(bubba_salary, uga_buga_salary))
# print(arithmetic1.my_sum(bubba_salary, uga_buga_salary))
# print(sum1(bubba_salary, uga_buga_salary))
# print(sum2(bubba_salary, uga_buga_salary,300))

from lesson9 import my_sum, very_important_func
print(my_sum(bubba_salary, uga_buga_salary))
very_important_func()
from lesson9.another_directory.another_one_directory.application import my_sum as another_my_sum
print(another_my_sum(bubba_salary, uga_buga_salary))

