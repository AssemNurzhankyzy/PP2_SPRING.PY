#Python variables and comments
#In this file legal and illegal type of variables: 

#Legal variables are:

myname = "Johnson" 
my_name = "John" 
_my_name = "J" 
myname = "Johny" 
MYNAME = "John" 
myname = "John"

#Illegal variables are: 

# 2myname = "John"
# my-name = "John"
# my name = "John"t

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #In the print() function, you output multiple variables, separated by a comma

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)  #+ operator to output multiple variables

x = 5
y = "John"
print(x, y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()  #variable outside of a function, and use it inside the function

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x) # Create a variable inside a function, with the same name as the global variable

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)