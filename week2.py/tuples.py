#Python Tuples
mytuple = ("apple", "banana", "cherry")

#Tuples are used to store multiple items in a single variable
#creating a tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) #Tuples allow duplicate values

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))# lenght of the tuple

#One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male") # tuple can contain different data types:

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # data type

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) #Using the tuple() method to make a tuple:

# Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # prints the second item

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # negative indexing

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])# returns 3,4,5th item

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

  #Update Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # adding items

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # adding a tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) # removing a tuplw item
 
 # Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

 # LOOP TUPLES
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

  #JOIN TUPLES
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multypling them: Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)