class Student:
    def __init__(self, roll, gpa):  # constructor
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print("Roll:", self.roll, "gpa:", self.gpa)


rahim = Student(22, 3.45)
rahim.display()
payer = Student(11, 5.00)
payer.display()
