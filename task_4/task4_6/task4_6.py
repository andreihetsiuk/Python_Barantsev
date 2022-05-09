length_tail = int(input("Enter the length of cat tail: "))
x = " "
print(f"*    *\n******\n* ** *\n*    *\n******\n  **  \n******\n*    *\n*    *\n"
      f"*    *\n******")
for i in range(length_tail):
    for k in range(2):
        print(f"{x*i}  **")
