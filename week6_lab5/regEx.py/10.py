import re
with open ("roow.txt", encoding="utf-8") as f:
    data = f.read()

match=re.sub(r"[A-Z]",'_',data)
print(match)