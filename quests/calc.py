a = int(input())
b = int(input())
sym = input()
if b == 0 and sym == "/":
    print("На ноль делить нельзя!")
elif sym == "/":
    print(a / b)
elif sym == "*":
    print(a * b)
elif sym == "+":
    print(a + b)
elif sym == "-":
    print(a - b)
else:
    print("Неверная операция")
