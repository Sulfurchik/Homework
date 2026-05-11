num = int(input())
max = 0

while num > 0:
    digit = num % 10
    if digit > max:
        max = digit
    num = num // 10

print(max)