def heads(head, legs):
    for i in range(1,head):
        if i*2 + (head-i)*4==legs:
            return f"chicken {i}, rabbits {head-i} "

head = int(input(" number of heads: "))
legs = int(input("number of legs: "))

print(heads(head, legs))