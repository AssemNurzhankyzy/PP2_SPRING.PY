# Strings
a = "Hello"
print(a)

#to assign a multiline string to a variable by using three quotes ot three single quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b = "Hello World"
print(b[3])

for x in "banana":
  print(x)   #loops through the letters banana

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

a= "Hello World"
print(a[3:7]) #Result will be: characters from position 3 to position 7 (not included). Result is: l0,

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())  #The upper() method returns the string in upper case/ lower fotlower one

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!", removes whitespaces

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

# add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."  #o insert characters that are illegal in a string, use an escape characte