print("Введите среднюю скорость Пети:")
PetaAVG = int(input())
print("Введите среднюю скорость Васи:")
VasaAVG = int(input())
print("Введите среднюю скорость Толи:")
TolaAVG = int(input())

prize = max(PetaAVG, VasaAVG, TolaAVG)

match prize:
    case a if PetaAVG == prize:
        print("Петя")
    case b if VasaAVG == prize:
        print("Вася")
    case c if TolaAVG == prize:
        print("Толя")