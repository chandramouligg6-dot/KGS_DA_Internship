# inverted special pyramaid

n = int(input("Enter a value: "))

for i in range(n, 0, -1):

    for k in range(n - i):
        print(" ", end="")

    for j in range(i * 2 - 1):
        print("*", end="")

    print()