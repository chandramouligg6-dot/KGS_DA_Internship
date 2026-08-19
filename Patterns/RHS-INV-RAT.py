# RHS Inverted Right-angle Triangle

n = int(input("Enter a value: "))

for i in range(1, (n + 1)):
    
    for k in range(1, i):
        print(" ", end="")
        
    for j in range(1, (n - i + 2)):
        print("*", end="")

    print()