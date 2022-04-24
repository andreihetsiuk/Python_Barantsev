col_par = int(input("введите количество пар:"))

max1 = 0
max2 = 0
max3 = 0
str1 = "str"
str2 = "str"
str3 = "str"
for k in range(col_par):
    str = input("введите название цветов: ")
    col_cvet = int(input("введите количество цветов:"))
    if col_cvet > max1:
        max3 = max2
        str3 = str2
        max2 = max1
        str2 = str1
        max1 = col_cvet
        str1 = str
    elif max1 > col_cvet > max2:
        max3 = max2
        str3 = str2
        max2 = col_cvet
        str2 = str
    elif max2 > col_cvet > max3:
        max3 = col_cvet
        str3 = str

print(str1)
print(str2)
print(str3)
