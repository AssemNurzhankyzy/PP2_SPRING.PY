def counter(n):
    return (i for i in range(n, -1, -1))

n = int(input("Enter a number: "))

for num in counter(n):
    print(num)
