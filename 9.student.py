"""
__gt__
__lt__
__ge__
__le__
__eq__
__ne__
Dunder methods for comparison 
"""


class Student:
    """Create an object of Student with various attributes and features"""
    def __init__(
        self, roll_no: int, name: str, gender: str, age: int = 0, phone_number: int = 0
    ) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number
    # def __init__(self) -> None:
    #     self.roll_no = int(input("Enter roll no = "))
    #     self.name = input("Enter name = ")
    #     self.gender = input("Enter gender = ")
    #     self.age = int(input("Enter age = "))
    #     self.phone_number = int(input("Enter phone = "))
        
    def __str__(self)-> str:   #This will print name and age of object created
        return f"{self.name} and {self.age}"
    
    def __add__(self, other): #This helps to add parameters of different objects 
        return self.age + other.age
    
    def __len__(self): 
        return len(str(self.phone_number))
    

    def __gt__(self, object2) -> bool: #Dunder method for comparision
        return self.age > object2.age

    def updateName(self) -> None:
        self.name = input("Enter new name = ")

    def updatePhoneNumber(self, new_number=0) -> None:
        self.phone_number = new_number

    def display(self) -> None:
        """Display all the info related to a Student"""
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone number = {self.phone_number}")

        

s1 = Student(1, "Anirudh", "Male", 26, 8969696569)
s2 = Student(2, "Vandana", "Female", 88, 9999658569)
print(len(s1))     

