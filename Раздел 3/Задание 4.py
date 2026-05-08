num = int(input())
while num <0:
    print("Введите неотрицательное цисло:")
    num = int(input())
factorial = 1

for i in range(1, num + 1):
    factorial *= i
print(factorial)