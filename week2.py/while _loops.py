# Python While Loops
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 9
  if i == 3:
    continue
  print(i+12)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")