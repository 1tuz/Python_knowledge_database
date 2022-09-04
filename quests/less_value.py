a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    res = a
else:
    res = b

if c < d:
    res_2 = c
else:
    res_2 = d

if res < res_2:
    print(res)
else:
    print(res_2)