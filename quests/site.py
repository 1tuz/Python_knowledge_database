import os

# Данная программа ожидает ввод сайта и определяет конструкцию ссылки.
while True:
    site = input("Введите адрес сайта:\n")

    if 'https://' in site:
        os.system('start ' + site)
        print('if')

    elif 'www.' in site:
        os.system('start ' + site)
        print('elif')

    elif 'https://' in site:
        os.system('start ' + site)
        print('elif2')

    elif 'Done' in site:
        break
        print("Работа завершена")

    else:
        site = 'https://www.' + site
        os.system('start ' + 'https://www.' + site)
        print('else')
