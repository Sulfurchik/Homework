import math
print("Введите число a:")
a = float(input())
print("Введите число b:")
b = float(input())
print("Введите число c:")
c = float(input())

D = b**2 - 4*a*c

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f'{x:.2f}')
else:
    if D < 0 :
        print("No solution")
    elif D == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")