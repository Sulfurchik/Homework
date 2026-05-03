print("Введите имя ребёнка:")
name = input()
print("Введите номер шкафчика:")
number = int(input())

last = number % 10
mid = number//10%10
first = number//100%10

print(f'Группа №{first}.\nНомер в группе: {last}. {name}.\nШкафчик: {number}.\nКроватка: {mid}.')
