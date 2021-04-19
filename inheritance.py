class Phone:  # Phone is  main class or perents class
    def Call(self):
        print("Please call your mom")

    def Meassage(self):
        print("Please message on your father")


class Samsung(Phone):  # there phone class inheritae  ########### samsung means sub class
    def endcall(self):
        print("please don't call your gf")


ss = Samsung()
ss.Call()
ss.Meassage()
ss.endcall()


# Inheritance example
# Inheritance 3 type .like 1.Hiera

class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("i am area method of shape class.")


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Aare of triangle :", area)


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of reactangle :", area)


# Triangle area call
T = Triangle(20, 30)
T.area()
# Reactangle area calling
R = Rectangle(30, 30)
R.area()
