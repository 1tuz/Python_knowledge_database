# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет интересное число или нет. Если число интересное, следует вывести – «Число
# интересное» иначе «Число неинтересное».
var = int(input())
last = var % 10
mid = var % 100 // 10
first = var % 1000 // 100
more = max(first, mid, last)
print("more = ", more)
less = min(first, mid, last)
print("min = ", less)
average = (last + mid + first) - more - less
print("avg = ", average)
if more - less == average:
    print("Число интересное")
else:
    print('Число неинтересное')