a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a < 0 and b < 0 or a > 0 and b > 0:
    print("same sign")
else:
    print("diff sign")
