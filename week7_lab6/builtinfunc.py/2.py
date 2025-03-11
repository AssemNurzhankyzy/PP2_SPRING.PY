def counterletter(letter):
    upper = 0
    lower = 0
    for i in letter:
        if "A" <= i <= "Z":
            upper += 1
        elif "a" <= i <= "z":
            lower += 1
    print("Sum of upper case:", upper)
    print("Sum of lower case:", lower)

sentence = input("Enter sentence: ")
counterletter(sentence)
