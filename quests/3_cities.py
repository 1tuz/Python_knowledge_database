# Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
# На вход программе подаётся названия трех городов, каждое на отдельной строке.
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
# Примечание. Гарантируется, что длины названий всех трех городов различны.
city1, city2, city3 = input(), input(), input()
lenght1, lenght2, lenght3 = len(city1), len(city2), len(city3)
less = min(lenght1, lenght2, lenght3)
more = max(lenght1, lenght2, lenght3)
if less == lenght1:
    print(city1)
elif less == lenght2:
    print(city2)
else:
    print(city3)

if more == lenght1:
    print(city1)
elif more == lenght2:
    print(city2)
else:
    print(city3)

# a, b, c = str(input()), str(input()), str(input())
# print(min(a, b, c, key=len ))
# print(max(a, b, c, key=len ))
# Alternative