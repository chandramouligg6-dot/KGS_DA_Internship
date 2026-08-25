# Inverted LHS Hollow Right-Angled Triangle Pattern

n = int(input("Enter a value: "))
for i in range(n,0,-1):
    for j in range(1,n+1):
        if i == n or j == 1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()