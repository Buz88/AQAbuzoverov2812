class Human:
    def __init__(self, name:str, age:int, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Employee(Human):
    def __init__(self, name, age, gender, job_position, salary):
        super().__init__(name, age, gender)
        self.job_position = job_position
        self.salary = salary

jonh = Human('John', 30, 'male')
evelyn  = Employee('Evelyn', 32, 'female', 'aqa', 4800)

class Donkey:
    strenght = 5

class Horse:
    speed = 10

class Mul(Horse, Donkey):
    pass

mul = Mul()
print(mul.speed)
print(mul.strenght)
