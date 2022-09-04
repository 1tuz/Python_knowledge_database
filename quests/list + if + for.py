n = list(range(1, 21))
b = n.copy()  # Копирование. Можно также использовать b = n[(start):(stop):(step)]
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(m)
    print(n)


# x = [9, 8, 7, 6, 5]
# x.append(4)  # Добавление 4
# x.sort()  # Сортирова списка по возрастанию
# x.remove()  # Перевернуть список
# print(x)
