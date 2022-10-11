import re


txt = "test -a"
regular = re.findall(r'^\w+', txt)
print(regular[0])



