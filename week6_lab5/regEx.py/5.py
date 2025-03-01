import re
with open ("roow.txt", encoding="utf-8") as f:
    data = f.read()

match = re.findall(r"a+.*b",data)
print(match)