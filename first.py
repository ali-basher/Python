import re

text = "a"
patt = "^[a-z]$"
v = re.match(patt, text)
print(v.group())
if v is None:
    print("No")
else:
    print("Yes")