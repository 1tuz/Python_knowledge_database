# На вход программе подаются два целых числа aa и bb (a \le b)(a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от aa до bb включительно, куб которых оканчивается на 44 или 99.
#
# Формат входных данных
# На вход программе подаются два целых числа aa и bb (a \le b)(a≤b).
#
# Формат выходных данных
# Программа должна вывести одно целое число в соответствии с условием программы.
a, b = int(input()), int(input())
c = 0
for i in range(a, b+1):
    if i % 10 == 4 or i % 10 == 9:
        c += 1
print(c)