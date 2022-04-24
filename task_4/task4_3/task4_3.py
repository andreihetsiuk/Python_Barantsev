action = input("Введите действие: ")
s = 0
while action != "Пришли полицейские":
    dish1 = int(input("Введите цену блюда: "))
    dish2 = int(input("Введите цену блюда: "))
    if s < 100:
        if dish1 >= dish2:
            s = s + dish1
        else:
            s = s + dish2
    else:
        if dish1 >= dish2:
            s = s + dish2
        else:
            s = s + dish1
    action = input("Введите действие: ")

if s >= 100:
    print(s)
else:
    print(20000 + s)
