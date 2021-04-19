# inherite clss 
class Rectangle: # Rectangle is perent/ base class
    def __init__(self):
        print("hello rectangle.")

    def area(self,x,y):
        return x * y


class Squre(Rectangle): # squre is sub class
    def __init__(self):
        print("hello Squre.")

    def area(self,x):
        return  Rectangle.area(self,x,x)

Re =Rectangle()
sq  = Squre()
area = sq.area(12)
print(area)

