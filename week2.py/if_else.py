#Python If ... Else

#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:  #The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:  #he else keyword catches anything which isn't caught by the preceding conditions.
  print("a is greater than b")

a = 12
b = 43
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or keyword is a logical operator, and is used to combine conditional statements:a = 200
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#if statements cannot be empty,
# but if you for some reason have an if statement with no content, 
# put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass