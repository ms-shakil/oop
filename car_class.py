class Car:
    name =""
    color =""
    def start(self):
        print("starting the engine.")

my_car = Car()
my_car.name ="lamborghini" #instance obj
Car.color = "black" # class obj
print(my_car.name)
print(my_car.color)
print(my_car.start())


## fixt attribute
class Mycar:
    def __init__(self,x,y):
        self.name = x
        self.color = x
    def Start(self):
        print("Name",self.name)
        print("Color",self.color) 
        print("This is my car")   

car = Mycar("lambourghini","Red")
car.Start()


        