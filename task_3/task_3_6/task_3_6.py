price_of_goose = int(input("enter price of goose: "))
quantity = int(input("enter quantity: "))

discount25 = 0.75
discount50 = 0.5

if 5 < quantity < 11:
    price_of_goose = quantity * price_of_goose * discount25

elif quantity > 10:
    price_of_goose = quantity * price_of_goose * discount50

else:
    price_of_goose = quantity * price_of_goose
print(int(price_of_goose))
