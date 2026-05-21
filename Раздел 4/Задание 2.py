N = int(input())
num = 1

rows = 0
temp = 0
while temp < N:
    rows += 1
    temp += rows

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(i):
        if num > N:
            break
        print(num, end=" ")
        num += 1
    print()