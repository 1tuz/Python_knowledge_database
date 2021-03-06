# Изменяемых стандартных типов в языке Python всего 3: список, словарь и множество. Список является изменяемым типом:
# Для списков гарантируется, что когда интерпретатор встретит в коде список он создаст для него новый объект: Это
# верно для всех изменяемых типов языка Python. Словари (dict) являются изменяемым типом данных.


class Mutable_vars:
    list_var = [1, 2.2, 'python']  # Список - один из самых используемых типов данных. Очень гибок.
    dict_var = {"name": "Antony", "age": 25, 1: 1}  # Словарь хранит данные в виде значение-ключ/вызов по ключу, а изменить можно только значение.
    set_var = {5, 2, 3, 1, 4}  # Множество - удаляет неуникальные значения.
