from math import sqrt
print("Введите координату x:")
x = float(input())
print("Введите координату y:")
y = float(input())

if x**2 + y**2 > 100:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
else:
    danger = False
    bottom = (x + 1) ** 2 / 4 - 9
    if -7 <= x <= -4:
        top = (5 / 3) * (x + 7)
    elif -4 <= x <= 0:
        top = 5
    elif 0 <= x <= 5:
        top = sqrt(25 - x**2)
    else:
        top = None

    if top and bottom <= y <= top:
        danger = True
    if danger:
        print("Опасность! Покиньте зону как можно скорее!")
    else:
        print("Зона безопасна. Продолжайте работу.")