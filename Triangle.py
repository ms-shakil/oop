class Triangle:
    def __init__(self, base, high):
        self.base = base
        self.high = high

    def area(self):
        ar = 0.5*self.base*self.high
        print("Area:", ar)


obj = Triangle(10, 20)
obj.area()
obj = Triangle(30, 40)
obj.area()
