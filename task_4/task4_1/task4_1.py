year_of_birth = int(input("enter year_of_birth: "))
year_of_birth = year_of_birth * 4
counter = 0
while year_of_birth > 0:
    div = year_of_birth % 10
    counter = counter + div
    year_of_birth = year_of_birth // 10
flag = True
print("Раз, два... Меркурий в четвертом доме... луна ушла... шесть –\nнесчастье... вечер – семь...")
if counter % 2 == 0:
    print("Вас ждет уважение.")
    flag = False
if counter % 8 == 0:
    print("Вы будете богат.")
    flag = False
if 9 < counter < 100:
    print("Вы проживете должгую жизнь")
    flag = False
if flag:
    print("Я не могу предсказать Вашу судьбу!")


