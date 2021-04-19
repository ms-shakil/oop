class Vehicle:
    """ Base class for all vehicles"""
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
    def drive(self):
        print("Driving",self.manufacturer,self.name)
    def  turn(self,direction):
        print("Turning",self.name,"to",direction)
    def brake(self):
        print(self.name," is stoping!")

class Car(Vehicle):
     """ car class"""
     def change_gear(self, gear_name):
        print(self.name,"is changing gear to ", gear_name)

if __name__ == "__main__":
    C = Car("Mustang 5.0 GT coupe","Ford","Red")
    C.drive()
    C.turn("Left")
    C.brake()
    C.change_gear("P")


##### base class mathode call on child class

class Base:
    """ Base class for all vehicles"""
    def __init__(self,name,manufacturer,color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


class Child(Base):
    """ child class"""
    def __init__(self,name,manufacturer,color,year):
        print("Creating a car")
        super().__init__(name,manufacturer ,color) # base clss proparty call by child cls
        self.year = 2021
        self.wheels = 4
if __name__ =="__main__":
    c = Child("Mus 5.0 Gt","ford","red",2021)
    print(c.name,c.year,c.wheels,c.color)        

