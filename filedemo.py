"""file =open ("students.txt","w")
file.write("ravi\n")
file.write("raju\n")
file.write("rani\n")
file.close()

print("file created successfully")

"""


"""file =open ("students.txt","r")
data=file.read()
print(data)
file.close()"""

"""file =open ("students.txt","a")
file.write("haasini\n")
file.close()
print("new student added")"""


with open("students.txt","r") as file:
    print(file.read())