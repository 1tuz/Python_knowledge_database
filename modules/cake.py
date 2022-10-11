import datetime
today = datetime.datetime.today().isoweekday()
stocks = ("Наполеон", "Детская мечта", "Клубничный пломбир", "Бородино", "Морковный чизкейк", "Смородиновый мусс", "NEW Медовик")
if today == 1:
    print(stocks[0])
elif today == 2:
    print(stocks[1])
elif today == 3:
    print(stocks[2])
elif today == 4:
    print(stocks[3])
elif today == 5:
    print(stocks[4])
elif today == 6:
    print(stocks[5])