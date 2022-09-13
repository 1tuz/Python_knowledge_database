# Назовем число красивым, если оно является четырехзначным и делится нацело на 77 или на 1717. Напишите программу,
# определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым,
# или «NO» в противном случае.
num = int(input())
if 9999 > num > 999 and (num % 7 == 0 or num % 17 == 0):
    print("YES")
else:
    print("NO")