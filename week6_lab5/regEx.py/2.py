import re
with open ("roow.txt", encoding="utf-8") as f:
    data = f.read()

matches = re.findall("a.*bb+|abbb+", data)
print(matches)
