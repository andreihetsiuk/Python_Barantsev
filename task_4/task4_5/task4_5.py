length_hill = int(input("Enter the length of hill: "))
initial_high = 0
max_current = 0

max_final = 0
for i in range(length_hill // 100):
    high = int(input("Enter the high: "))

    if high > initial_high:
        max_current = max_current + 1
        initial_high = high
        if max_current > max_final:
            max_final = max_current
    else:
        max_current = 0
        initial_high = high
print(max_final*100)
