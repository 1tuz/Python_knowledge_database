import os

# Данная программа ожидает ввод адреса сайта и определяет конструкцию ссылки.
# Она работает до тех пор, пока не ввести 'Done' в терминале.
while True:
    site = input("Введите адрес сайта :\n")

    if 'https://www.' in site:
        os.system('start ' + site)
        print('Открываем', site)

    elif 'www.' in site:
        os.system('start ' + site)
        print('Открываем', site)

    elif 'https://' in site:
        os.system('start ' + site)
        print('Открываем', site)

    elif 'Done' in site:
        print("Завершение работы программы.")
        break

    else:
        var = site != 'https://www.' + site
        os.system('start ' + 'https://www.' + site)
        print('Открываем https://www.'+site)
