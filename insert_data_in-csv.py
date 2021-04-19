import csv
class Students:
   
   def __init__(self,Id,Name,Age,dist):
     self.Id=Id
     self.Name=Name
     self.Age=Age
     self.dist=dist

   def get_information(self):
     return{
       "ID":self.Id,
       "Name":self.Name,
       "Age":self.Age,
       "Dist":self.dist
     }
list_of_students=[]
def find_student(Id):
  for i in list_of_students:
    if i.Id == Id:
      return i.get_information()
  return "ID not found"         
with open("./abcd.csv","w")as f:
   data=f.write("{}\n".format(list_of_students))
#   lines=data.split("\n")
#   for r in lines:
#     [Id,Name,Age,dist]=r.split(',')
#     p=Students(Id,Name,Age,dist) 
#     list_of_students.append(p)
# get_id=input("enter ID:")
# print(find_student(get_id))
data=int(input("enter an number:"))
for i in range(data):
  id=input("enter an person id{0}:".format(i))
  name=input("enter an person Name{0}:".format(i))
  age=input("enter an person age{0}:".format(i))
  dist=input("enter an person dist{0}:".format(i))
with open("./abcd.csv","r") as f: 

  list_of_students.append(Students(id,name,age,dist))


print(list_of_students)
