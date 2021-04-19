
#  there have 2 class with out define object
class First_class:
    name ="royel coach"
    color = "black"

    def data():
        print("hello oop")

print("car name",First_class.name)        
print("car color", First_class.color)
First_class.data()

# attribute  change able code

class Car:
    name =""
    color =""
    def Start():
        print("Starting the engine.")



Car.name = "volbo"
Car.color ="white"
print("Name of the car",Car.name)
print("Color of the car",Car.color)
Car.Start()
print(dir(Car))
