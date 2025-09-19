# Abstraction
from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("I have created perimeter")
        # return super().perimeter()

    def area(self):
        print("I have created area")



obj = Circle(7)
obj = Square(12) # when we call it provide error because we use abstract method in class and it have no function of perimeter and area