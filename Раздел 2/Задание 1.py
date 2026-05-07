print("Как Вас зовут?")
name = input()
print (f'Здравствуйте, {name}!\nКак дела?')
mood = input()
match mood:
    case "Хорошо":
        print("Я за вас рада!")
    case "Плохо":
        print("Всё наладится!")