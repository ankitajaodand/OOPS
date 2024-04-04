'''Whenever we create object init method is always called by default so whatever is the cumpulary for all the objects we can 
write that in the init'''

'''In the file before classes-objects, we definately need attributes to be set for all methods to execute anything or any other method 
 on the method'''

class Student:

    def __init__(self): #Dunder Method, whenever we create the object this is called by default
        print("INIT")
        self.roll_no = int(input("Enter roll no = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))
        self.phone_number = int(input("Enter phone = "))


    def display(self) -> None:
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone number = {self.phone_number}")

s1 = Student()
s1.display()