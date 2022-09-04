# while условное выражение:

# Пример 1
number = 1

while number < 5:
    print(f"number = {number}")
    number += 1
else:  # опционально
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

# Пример 2
x = 0

while x < 5:
    print('Not enough = ', x)
    x += 1
else:
    print("OK = ", x)

# Пример 3
while True:
    a = int(input('Введите число\n'))
    count = 0
    b = 1

    while count < a:
        count += 1
        b *= count

    else:
        print(b)

# Пример 4
c = ''
while len(c) < 5:
    d = input()

    c += d

else:
    print(c)
