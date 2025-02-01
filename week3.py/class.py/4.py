import math

class Coordinate:
    def __init__(self, x_val, y_val):
        self.x_val = x_val
        self.y_val = y_val

    def display(self):
        print(f"Coordinates: ({self.x_val}, {self.y_val})")

    def shift(self, new_x, new_y):
        self.x_val = new_x
        self.y_val = new_y

    def calculate_distance(self, other_point):
        diff_x = self.x_val - other_point.x_val
        diff_y = self.y_val - other_point.y_val
        return math.sqrt(diff_x**2 + diff_y**2)

x_coord = float(input("Enter x: "))
y_coord = float(input("Enter y: "))
first_point = Coordinate(x_coord, y_coord)
second_point = Coordinate(x_coord, y_coord)

first_point.display()
new_x = float(input("Enter new x: "))
new_y = float(input("Enter new y: "))
first_point.shift(new_x, new_y)
first_point.display()

distance_value = first_point.calculate_distance(second_point)
print(f"Distance between first_point and second_point: {distance_value}")
