a = input()
b = input()

if (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
    print("оранжевый")
elif (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
    print("фиолетовый")
elif(a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
    print("зеленый")
elif a or b == 'красный' or 'желтый' or 'синий' and a == b:
    print(a)
elif a or b == 'красный' or 'желтый' or 'синий' and a == b:
    print(a)
else:
    print("ошибка цвета")