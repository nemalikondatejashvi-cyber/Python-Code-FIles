"""name="sri vani"""

#open("filename","mode")

#file=open("data.txt","r")

#filemodes
"""
r -> read files
w ->write files

a -> append files
x->create new file

"""

file = open("data.txt","r")

data = file.read()

print(data)
 
file.close()