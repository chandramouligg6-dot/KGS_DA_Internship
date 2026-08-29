# Hollow butterfly
# Logic-1

n = int(input("Enter a value: "))

noc = 1
nor = (n * 2) - 1

for i in range(1, (n * 2)):
    for j in range(1, (n * 2)):
        if j == 1 or j == (n * 2) - 1 or j == i or j == (n * 2) - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1



# Hollow Butterfly Pattern
# Logic-2

n = int(input("Enter a value: "))

noc = 1
nor = (n * 2) - 1

for i in range(1, n * 2):
    for j in range(1, n * 2):
        if j == 1 or j == noc or j == nor or j == (n * 2) - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    if i < n:
        noc += 1
        nor -= 1
    else:
        noc -= 1
        nor += 1