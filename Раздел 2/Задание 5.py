print("Введите трёхзначное число:")
number = int(input())

last = number % 10
mid = number//10%10
first = number//100%10

crypt1 = mid + last
crypt2 = mid + first
crypt_first = max(crypt1, crypt2)
crypt_last = min(crypt1, crypt2)

print(str(crypt_last)+ str(crypt_first))