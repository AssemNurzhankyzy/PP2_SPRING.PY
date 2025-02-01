def histogram(int):
    for i in int:
        print ("*"* i )

integers = input(" Please enter the list of numbers:")
list=list(map(int,integers.split()))

histogram (list)