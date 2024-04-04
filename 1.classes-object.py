class Student: #Creating Class Student
    '''When we create object all the attributes will be associated objects by default with the default values when not updated 
    individually '''  
    roll_no = 0 #These class variables are called as data members or attributes
    name = ""
    gender = ""
    age = 0
    

    def setInfo(self): #Self is nothing but the object that will be calling the method
        '''This overwrites the default value of attributes for objects that are calls this method
        if we dont call this method for an object then it's attributes will be default'''
        self.roll_no = int(input("Enter roll no = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))

    def display(self):
        '''Prints the attributes of the method that is called'''
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")

print(Student.__doc__) #This will display the information about the class that you have written just after entering the class in the docstring
print(Student.display.__doc__) #This will display the information written on the method
s1 = Student() #creating object of class Student


s1.setInfo()
s1.display()


'''We dont need to define attributes default they can be created directly in the method setInfo()
However if we call Method display before SetInfo then it will fail '''
class Student: #Creating Class Student
    '''When we create object all the attributes will be associated objects by default with the default values when not updated 
    individually '''  

    def setInfo(self): #Self is nothing but the object that will be calling the method
        '''This overwrites the default value of attributes for objects that are calls this method
        if we dont call this method for an object then it's attributes will be default'''
        self.roll_no = int(input("Enter roll no = "))
        self.name = input("Enter name = ")
        self.gender = input("Enter gender = ")
        self.age = int(input("Enter age = "))

    def display(self):
        '''Prints the attributes of the method that is called'''
        print(f"Roll no = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")

s1=Student()        
s1.display() #this will fail because we didnt set the attributes: AttributeError: 'Student' object has no attribute 'roll_no'



