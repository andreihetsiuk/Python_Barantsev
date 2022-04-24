type_of_transfer = int(input("enter type of transfer: "))
if type_of_transfer == 1:
    rate_rub = int(input("enter rate rub/gold: "))
    rate_gold = int(input("enter rate gold/usd : "))
    summ_to_transfer = int(input("enter summ to transfer: "))
    summ = summ_to_transfer * rate_rub
    summ = summ / rate_gold
    print(str(summ_to_transfer) + " " + "rubles" +" " "is" " "+ str(summ) + "$")
elif type_of_transfer == 2:
    rate_rub = int(input("enter rate rub/gold: "))
    rate_gold = int(input("enter rate gold/usd : "))
    summ_to_transfer = int(input("enter summ to transfer: "))
    summ = summ_to_transfer * rate_gold
    summ = summ / rate_rub
    print(str(summ_to_transfer) + "$" +" " "is" " "+ str(summ) + " " + "rubles")
else:
    print("wrong type of transfer")


