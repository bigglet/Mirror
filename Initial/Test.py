print("Hello World")

def name_of_function(para): #Defines a function
    return para

def name_of_procedure(): #Defines a procedure - don't need to label eg void
    print("String")

print(name_of_function("String"))

print(name_of_function(12))

var = 12
var2 = "String"
var = "String"
print(var, var2)

if 2*5 == 10:
    print("True")

for i in range(0,10):
    print(i)

print()

j = 0
while j < 10:
    print(j)
    j+=1

#Commenting
#Switch / Case doesn't exist

print("Insert variables into text: {0} and {1}".format(12, "String"))

#To import a library eg re:
import re
