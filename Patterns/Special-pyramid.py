# Special Pyrmaid 

n = int(input("Enter a value: "))

for i in range(1, (n + 1)):
    for k in range(n , i, -1):
        print(" ",end="")
    for j in range(1,(i * 2)):
        print("*",end="")
    print()