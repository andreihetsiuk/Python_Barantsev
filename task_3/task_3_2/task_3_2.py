a = int(input("enter 1st weight: "))
b = int(input("enter 2st weight: "))
c = int(input("enter 3st weight: "))
d = int(input("enter 4st weight: "))

if a > b and a > c and a > d:
    print("here it is 1")
elif b > a and b > c and b > d:
    print("here it is 2")
elif c > a and c > b and c > d:
    print("here it is 3")
elif d > a and d > b and d > c:
    print("here it is 4")
else:
    print("no brills")