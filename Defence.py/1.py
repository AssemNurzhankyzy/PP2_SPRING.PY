def letter_generator(s):
    for char in s:
        if char.isalpha(): 
            yield char


for letter in letter_generator("Hello, World! 123"):
    print(letter)