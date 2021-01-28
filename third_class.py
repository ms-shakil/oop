# instance attibute
class Car:
    def __init__(self,S,R):
        self.name = S
        self.color = R

    def Start(self):
        print("car name",self.name)
        print("car color",self.color)
        print("start the car") 

Object1 =Car("volbo","read")
# if we want to create new attibute
Object1.year =322
print(Object1.year)
Object1.Start()  
Ob2 = Car("royel","white")
Ob2.Start()        
        