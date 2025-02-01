def permutations(p): 
    n = len(p)

    for i in range(n):
        for j in range(n):
            print(p[(j-i)], end=" ")
        print()
        
pr =str(input("Enter one word :" ))
permutations( pr) 