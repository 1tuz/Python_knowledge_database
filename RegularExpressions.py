import re
import datetime


age = int(input("Введите свой год рождения в формате гггг.мм.дд"))


def ageInYears( d ):
    today = datetime.date.today()
    currentYrAnniversary = datetime.date( today.year, d.month, d.day )
    return (today.year - d.year) - (1 if today < currentYrAnniversary else 0)

ageInYears()
print(age)

