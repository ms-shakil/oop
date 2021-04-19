# class object support attribute reference and instantiation
# attribute reference
# class Squre:
#     side = 5

#     def start():
#         print("hello bangladesh") 
# print(Squre.side)
# Squre.start()


# instantiation 

inp =int(input("Enter the number:"))
class Squre:
    def __init__(self,value):
        self.side = value 

    def area(self):
        return self.side * self.side


sq = Squre(inp)

print(sq.area())        
