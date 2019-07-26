class Person:
    def __init__ (self):
        print("Person created")
    def walk(self):
        print('Person walking in person class')
class Employee(Person):
    def __init__(self):
        print("Employee created")
        super().__init__()
    def Assign_designation(self):
        print("Designation Assigned")
    def walk(self):
        pass

#we use pass keyword to declare abstract function
#we have to use super function to call the constructor of the base class like super.__init__()
p1=Person()
p1.walk()
e1=Employee()
e1.Assign_designation()
e1.walk()

