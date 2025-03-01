import re
with open ("roow.txt", encoding="utf-8") as f:
    data = f.read()

match= re.sub(r"[., ]",':',data)
print(match)