# Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни
a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
if D < 0:
    print("Нет корней")
elif D == 0:
    print(-b / (2 * a))
else:
    x1 = (-b - D ** 0.5)/(2*a)
    x2 = (-b + D ** 0.5) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))