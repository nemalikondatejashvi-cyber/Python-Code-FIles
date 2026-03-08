"""class Student:#class
    name="rupa"
    age=24
"""
"""class student:
    name="rupa"
    age= 21

s1 = student()

print(s1.name)
print(s1.age)
"""
"""class Bank:

  def__init__(self):
        self.balance=1000
    
def show_balance(self):
        print(self.balance)

b=Bank()
b.showbalance()      
    """

#__init__()#constructor

"""class Student:

    def __init__(self,name,age):
     self.name= name  
     self.age = age 

s1=Student("kiran",25)
print(s1.name)
print(s1.age)    """

"""class Student:

    def __init__(self,name):
     self.name= name  
    def show(self):
       print("Student Name:", self.name)

s1=Student("kiran")

s1.show()"""

#ECAPSULATION

"""class Bank:#class

    def __init__(self):#constructr
        self.balance=1000

    def show_balance(self):
        print("balance:",self.balance)

b=Bank()

b.show_balance()"""

#inheritance
#parent-> child


"""class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    pass
d=Dog()

d.speak()"""

"""class Bird:
     
     def sound(self):
          print("Bird makes sound")

class parrot(Bird):
     
     def sound(self):
          print("parrot talks")

p=parrot()
p.sound()"""

#ABSTRACTION 

class car:
    def start(self):
        print("car started")

c= car()

c.start()
       