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


class DTEKEmployee(Employee):
    def __init__(self):
        super().__init__(3000, 'welder')

    def do_work(self):
        print('I am welder from DTEK!')


mykola = DTEKEmployee()
mykola.do_work()
mykola.chill()
#employee = Employee(1,'a')

class Car(ABC):

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        self.wheels = 4
        self.engine = True
        self.engine_type = None
    def move_forward(self):
        print('I am moving forward')
    def move_backward(self):
        print('I am moving backwards')
    def turn_left(self):
        print('I am turning left')
    def turn_right(self):
        print('I am turning right')

    @abstractmethod
    def refuel(self):
        pass

class Toyota(Car):
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.engine_type = 'DVS'

    def refuel(self):
        print('I am refueling with diesel')

class Tesla(Car):
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.engine_type = 'Electric'
    def refuel(self):
        print('I am refueling with electricity')

toyota = Toyota('red',300)
toyota.refuel()
toyota.turn_left()
tesla = Tesla('blue',300)
tesla.refuel()
tesla.move_forward()