# usr/bin/env python3
# first 2 input take data and 3rd  input show data

class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_information(self):
        return{
            "name": self.name,
            "age": self.age,
            "id": self.id}


list_of_Student = []


def find_inpormation(id):
    for s in list_of_Student:
        if s.id == id:
            return s.get_information()
    return "Id dont mess"


data = int(input("enter an number:"))
for i in range(data):
    id = input("enter an person id{0}:".format(i))
    name = input("enter an person Name{0}:".format(i))
    age = input("enter an person age{0}:".format(i))

    list_of_Student.append(Student(id, name, age))

in_id = input("enter an id:")
print(find_inpormation(in_id))
