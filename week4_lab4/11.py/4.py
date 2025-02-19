def squares(a, b):
    return (i * i for i in range(a, b + 1))

a = int(input("Enter the start number: "))
b = int(input("Enter the end number: "))

for square in squares(a, b):
    print(square)
