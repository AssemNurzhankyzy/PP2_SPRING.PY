llist=input("size list:")

my_list=list(map(int,llist.split()))
multiply = 1
for i in my_list:
    multiply*=i

print(multiply)