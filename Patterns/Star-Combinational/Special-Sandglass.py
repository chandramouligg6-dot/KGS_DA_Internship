n = int(input("Enter the number: "))
print("Hourglass Pattern")

noc = n
for i in range(1, n * 2):
    for k in range(n - noc):
        print(" ", end="")
    
    for j in range(1, noc * 2):
        print("*", end="")
    
    print()
    
    if i < n:
        noc -= 1
    else:
        noc += 1