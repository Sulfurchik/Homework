print("Введите число N:")
N = int(input())
print("Введите число M:")
M = int(input())

peta = 7 - 3 + 2 + N
vasa = 6 + 3 - 2 + M
bigger = max(peta, vasa)
match bigger:
    case a if bigger == peta:
        print("Петя")
    case b if bigger == vasa:
        print("Вася")