"""def greet():
    print("hello welcome to python")#indentation
    greet()

"""

"""def multiply(a,b):
    result = a * b
    return result
answer = multiply(4,5)
print(answer)"""

#types of functions

"""
builtin functions
print()
len()
type()
input()
sum()

"""

"""numbers =[10,20,30,40]

print(len(numbers))
print(type(numbers))
print(sum(numbers))"""

 #user defined function 2

"""def checkresult(marks):
    if marks >=35:
        return "pass"
    else:
        return"Fail"
result = checkresult(60)
print(result)        """

#lamda function =small anonymous function

"""def square(n):
    return n*n

result =square(5)
print(result)"""

"""square =lambda n: n*n

print(square(5))"""

#recursion function

"""def numbers(n):
    if n==2:
        return
    print(n)
    numbers(n-1)

numbers(5)# n =5,print 5 numberss(4)"""


#arguments in python

"""def greet(name):
    print("hello",name)

greet("rama")
greet("sita")
"""

#types of arguments

#4 types=positional,keyword,default,variable
 

 #positional =order
"""def student(name,course):
     print("Name:",name)
     print("Course:", course)

student("Python","vamshi")

"""

#keyword 

"""def student(name,course):
    print("Name:",name)
    print("course:",course)

student(course="Python",name="ravi")"""

#default 

"""def greet(name="Guest"):
    print("hello",name)
greet("vaishu")
greet("sowmya")"""

#variable length 

def totalmarks(*marks):
    print("marks:",marks)

totalmarks(85,90,78)
totalmarks(60,70)