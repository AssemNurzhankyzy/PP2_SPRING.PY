import math
num_sides = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of each side: "))

area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))

print("The area of the regular polygon is:", int(area))
