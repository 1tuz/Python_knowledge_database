s = str(input())
for i in set(s):
    if s.count(i) > 1:
        s = s.replace(i, ')')
    else:
        s = s.replace(i, '(')
print(s)

