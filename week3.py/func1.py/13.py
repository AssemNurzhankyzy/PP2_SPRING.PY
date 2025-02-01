from random import randint

def guessthenumber(): 
    print("Hello! What is your name?")
    name = input("Enter your name: ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    run = True
    sum = 0
    
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")

guessthenumber()