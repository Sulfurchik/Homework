left = 1
right = 1000

while True:
    middle = (left + right) // 2

    print(middle)
    answer = input()

    if answer == "Угадал!":
        break
    if answer == "Больше":
        left = middle + 1
    if answer == "Меньше":
        right = middle - 1