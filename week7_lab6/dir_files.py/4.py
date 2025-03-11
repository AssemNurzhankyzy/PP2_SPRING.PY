import os
import string

with open("some.txt") as f:
    data = f.read()  

print(len(list(data.split("\n"))))
f.close()