class Cat:
    def make_noise(self):
        pass

class Lion(Cat):
    def __init__(self):
        self.color = 'Yellow'
        self.tail = 'Long'

    def make_noise(self):
        print('Lion makes roar')

class Tiger(Cat):
    def __init__(self):
        self.color = 'Orange'
        self.tail = 'Long'

    def make_noise(self):
        print('Tiger from 3th OSHB')

class Puma(Cat):
    def __init__(self):
        self.color = 'Black'
        self.tail = 'Short'

    def make_noise(self):
        print('Buy new shoes!')

lion = Lion()
lion.make_noise()
tiger = Tiger()
tiger.make_noise()
puma = Puma()
puma.make_noise()


