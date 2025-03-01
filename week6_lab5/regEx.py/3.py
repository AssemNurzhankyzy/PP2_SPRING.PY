import re
with open ("roow.txt", encoding="utf-8") as f:
    data = f.read()

matches = re.findall("[a-z]_+[a-z]+", data)
print(matches)
