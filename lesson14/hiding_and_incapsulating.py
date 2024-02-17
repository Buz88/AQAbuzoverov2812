from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
    @abstractmethod
    def do_work(self):
        pass

    def chill(self):
        print('I am chilling')


class Engineer(Employee):
    def __init__(self):
        super().__init__(4000, 'Engineer')

    def _deploy_programm(self):#private
        print('I am deploying')

    def __create_framework(self):#protected __ ne maemo do niogo dostupu i naschadki i zovni
        print('I am creating')

    def __create_infrastructure(self):
        print('I am creating infrastructure')

    def deploy(self):
        self.__create_infrastructure()
        self.__create_framework()
        self._deploy_programm()

    def do_work(self):
        print('I am creating new framework')

class Developer(Engineer):
    def __init__(self):
        super().__init__()

    def do_work(self):
        print('I am writing new programs using this framework')
        self._deploy_programm()
        self.deploy()

dev = Developer()
dev.do_work()

class Human():
    def __init__(self, name:str, age:int):
        self.__hidden_name = name
        self._age = age

    @property
    def name(self):
        return self.__hidden_name

john = Human('John', 30)