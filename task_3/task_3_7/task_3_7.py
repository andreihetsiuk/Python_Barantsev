role1 = (input("enter 1 role: "))
role2 = (input("enter 2 role: "))
role3 = (input("enter 3 role: "))

child_price = 5
prof_price = 10
non_prof_price = 30
police = 5

if role1 == "child":
    price1 = child_price
elif role1 == "prof":
    price1 = prof_price
elif role1 == "non prof":
    price1 = non_prof_price
elif role1 == "police":
    price1 = police
if role2 == "child":
    price2 = child_price
elif role2 == "prof":
    price2 = prof_price
elif role2 == "non prof":
    price2 = non_prof_price
elif role2 == "police":
    price2 = police
if role3 == "child":
    price3 = child_price
elif role3 == "prof":
    price3 = prof_price
elif role3 == "non prof":
    price3 = non_prof_price
elif role3 == "police":
    price3 = police
print(price1 + price2 + price3)
