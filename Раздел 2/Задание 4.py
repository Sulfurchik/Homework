print("Введите число:")
number = int(input())
last = number % 10
mid1 = number//10%10
mid2 = number//100%10
first = number//1000%10

find = str(last) + str(mid1) + str(mid2) + str(first)
if int(find) == number:
    print("YES")
else:
    print("NO")