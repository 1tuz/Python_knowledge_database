import os

site = input()

if 'https://' in site:
    os.system('start ' + site)
    print('if')

elif 'www.' in site:
    os.system('start ' + site)
    print('elif')

elif 'https://www.' in site:
    os.system('start ' + site)
    print('elif2')

else:
    site != 'https://www.' + site
    os.system('start ' + site)
    print('else')
