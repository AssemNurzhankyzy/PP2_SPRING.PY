#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  #Print each fruit in a fruit list:

for x in "banana":
  print(x)  #Loop through the letters in the word "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
   print(x)

for x in range(2, 6):
  print(x)  #Using the start parameter:

for x in range(2, 30, 3):
  print(x)  #Increment the sequence with 3 (default is 1):

for x in range(6):
  print(x)
else:
  print("Finally finished!") #Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)  #Nested Loops

#for loops cannot be empty,
# but if you for some reason have a for loop with no content,
# put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass
