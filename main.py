# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from math import sqrt

def task1():
    name = input("Введите имя: ")
    password = input("Введите пароль: ")
    age = input("Введите возраст: ")
    print(f"имя - {name}, пароль - {password}, возраст - {age}")

def task2():
    time_user = int(input("Введите время в секундах: "))
    print(f"{time_user//3600}:{time_user//60}:{time_user}")

def task3():
    number = input("Введите число: ")
    print(f"n + nn + nnn = {int(number) + int(number+number) + int(number+number+number)}")

def task4():
    revenue = int(input("Введите выручку: "))
    costs = int(input("Введите издержки: "))
    employee = int(input(f"Введите количество сотрудников: "))
    if ((revenue - costs) > 0):
        print(f"Финансовый результат - прибыль. Ее величина = {revenue - costs}")
        print(f"Рентабельность выручки = {(revenue - costs) / revenue}")
        print(f"Прибыль фирмы в расчете на одного сотрудника = {(revenue - costs) / employee}")
    elif ((revenue - costs) == 0):
        print(f"Финансовый результат - выход в ноль.")
    else:
        print(f"Финансовый результат - убыль. Ее величина = {revenue - costs}")
        print(f"Рентабельность выручки = {(revenue - costs) / revenue}")
        print(f"Убыль фирмы в расчете на одного сотрудника = {(revenue - costs) / employee}")

def task5():
    day = int(input("Введите день недели: "))
    while (day > 7 or day < 1):
        day = int(input("Введите день недели: "))
    if (day == 6 or day == 7):
        print("Выходной")
    else:
        print("Не выходной")

def task6():
    x = True
    y = False
    z = True
    if ((-(x or y or z)) == (-x and -y and -z)):
        print("Верно")
    else:
        print("Ложь")

def task7():
    x = int(input("Введите x: "))
    while(x == 0):
        x = int(input("Введите x: "))
    y = int(input("Введите y: "))
    while (y == 0):
        y = int(input("Введите y: "))
    if(x>0 and y > 0):
        print(1)
    elif(x>0 and y < 0):
        print(4)
    elif(y>0):
        print(2)
    else:
        print(3)

def task8():
    coordinat = int(input("Введите четверть координат: "))
    if (coordinat == 1):
        print("x > 0, y > 0")
    elif (coordinat == 4):
        print("x > 0, y < 0")
    elif (coordinat == 2):
        print("x < 0, y > 0")
    else:
        print("x < 0, y < 0")

def task9():
    x1 = int(input("Введите x первой точки: "))
    y1 = int(input("Введите y первой точки: "))
    x2 = int(input("Введите x второй точки: "))
    y2 = int(input("Введите y второй точки: "))
    if (x1 < x2):
        x_buf = x1
        x1 = x2
        x2 = x_buf
    if (y1 < y2):
        y_buf = y1
        y1 = y2
        y2 = y_buf
    x_side_tri = x1 - x2
    y_side_tri = y1 - y2

    print(f"Расстояние {sqrt(x_side_tri * x_side_tri + y_side_tri * y_side_tri)}")

while True:
    a = int(input("Введите номер задачи:"))
    if(a == 1):
        task1()
    elif(a == 2):
        task2()
    elif (a == 3):
        task3()
    elif (a == 4):
        task4()
    elif (a == 5):
        task5()
    elif (a == 6):
        task6()
    elif (a == 7):
        task7()
    elif (a == 8):
        task8()
    else:
        task9()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
