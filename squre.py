class Squre:
    side = 3 # properties
    def area(self): # methodes
        return self.side * self.side

obj = Squre()

print(obj.area())  
print(Squre.area(obj))      

# #
class SSqure:
    side = 0
    def __init__(self,x):
        self.side = x

    def area(self):
        return self.side * self.side
sq = SSqure(5)

print(sq.area())            