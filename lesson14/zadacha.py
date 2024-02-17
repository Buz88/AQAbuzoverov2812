from abc import ABC, abstractmethod

class Road(ABC):
    def __init__(self,coverage):
        self.coverage = coverage
        self.__road_width = 4.2
    @abstractmethod
    def build_range(self):
        pass
    def lines_amount_count(self):
        return self.__road_width / 2

    @property
    def road_width(self):
        return self.__road_width

    @road_width.setter
    def road_width(self, road_width):
        self.__road_width = road_width

class Gruntovka(Road):
    def __init__(self):
        super().__init__('Gruntovka')
    def build_range(self,km):
        print(f'I am Gruntovka in Kyiv {km} km')

    def lines_amount_count(self):
        return self.road_width

class Sand(Road):
    def __init__(self):
        super().__init__('Sand')

    def __repair_bitum(self):
        print(f'I am repairing bitum')

    def build_range(self, km):
        self.__repair_bitum()
        print(f'I am sand road in Kharkiv {km} km')



    def lines_amount_count(self):
        return self.road_width

sand = Sand()
sand.build_range(10)
print(sand.road_width)
sand.lines_amount_count()
gruntovka1 = Gruntovka()
gruntovka1.build_range(123)
sand.road_width = 545
print(sand.road_width)