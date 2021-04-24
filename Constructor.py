class Student:
    def __init__(self, roll, gpa):  # constructor
        self.roll = roll
        self.gpa = gpa

    def __str__(self):
        return ("Roll = {self.roll} gpa =  {self.gpa}")

    def display(self):
        print("Roll: {self.roll}, gpa:,{ self.gpa}")


rahim = Student(22, 3.45)

print(rahim)
