print("Введите размер таблицы умножения:")
N = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(f"{i} * {j} = {i * j}")
    print()
