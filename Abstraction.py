from abc import abstractmethod


class Shape(ABC):  # abstract class  # this class for just model
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Aare of triangle :", area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of reactangle :", area)
# abstract class dose't soupport  object


# Triangle area call
T = Triangle(20, 30)
T.area()
# Reactangle area calling
R = Rectangle(30, 30)
R.area()
