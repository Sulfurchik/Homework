print("Введите число N:")
N = int(input())
print("Введите число M:")
M = int(input())
print("Введите число 1K1:")
K1 = int(input())
print("Введите число 2K2:")
K2 = int(input())

Answer1 = (M - K2) * N // (K1 - K2)
Answer2 = N - Answer1

print(Answer1, Answer2)