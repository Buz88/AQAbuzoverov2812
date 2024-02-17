
'''
class Human:
        name ='John'
        age = 30
        friends = []


class Dog:
    owner_friends = []


john = Human()
evelyn = Human()

print(john.name, john.age)
print(evelyn.name, evelyn.age)
john.name = 'john1'
evelyn.name = 'evelyn'
print(john.name, john.age)
print(evelyn.name, evelyn.age)
john.friends.append('Mike')
evelyn.friends.append('Julia')
print(john.friends)
print(evelyn.friends)
good_boy = Dog()
good_boy.owner_friends += evelyn.friends
print(f'good boy owner friends:{good_boy.owner_friends}')'''

class Human:
    def __init__(self, name:str, age:int, salary:float, job_position:str, hair_color:str):
        self.name = name
        self.age = age
        self.salary = salary
        self.job_position = job_position
        self.hair_color = hair_color

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    @classmethod
    def from_name_and_age(cls, name:str, age:int):
        return cls(name, age, None, None, None)
    @staticmethod #самодостатній не має прямого доступу ні до методів ні до параметрів
    def count_bonus(salary):
        return salary*1.2

john = Human.from_name_and_age('john',30)
evelyn = Human.from_name_and_age('Evelyn',32)
evelyn.salary = 4000
print(john.get_name(), john.get_age())
print(evelyn.get_name(), evelyn.get_age())
print(evelyn.count_bonus(evelyn.salary))
