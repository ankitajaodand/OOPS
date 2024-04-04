'''Class parameters are passed from the init only'''


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
s1 = Student(14, "Anirudh", "Male", 44, 998899889)
print(s1)
s2 = Student(name="Anirudh", age=99, gender="Male", roll_no=44, phone_number=333333)
s1.display()



'''By default if you print the object created it displays object and it's memory however we can update that using below dunder method
def __str__(self)-> str:  
    return "I am an object" 
In this code when you print object it will return "I am an object" instead of  <__main__.Student object at 0x1066bcee0>   '''

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
s1 = Student(14, "Anirudh", "Male", 44, 998899889)
print(s1) #Now this returns name and age of s1 since we have defined __str__
s2 = Student(name="Anirudh", age=99, gender="Male", roll_no=44, phone_number=333333)
s1.display()