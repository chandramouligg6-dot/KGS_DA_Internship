# Inverted RHS Hollow Right-Angled Triangle Pattern.

n = int(input("Enter a Value: "))

for i in range(1, n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(n, i-1, -1):
        if i == 1 or j == n or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()