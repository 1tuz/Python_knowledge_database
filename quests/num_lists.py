# Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно удовлетворяющие хотя бы одному из условий:
#
# число кратно 17;
# число оканчивается на 9;
# число кратно 3 и 5 одновременно.
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 15 == 0 or i % 10 == 9:
        print(i)