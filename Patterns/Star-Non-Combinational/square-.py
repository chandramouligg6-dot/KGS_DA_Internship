# Square Pattern

n = int(input("Enter the number: "))
#multiple rows
for i in range(1,(n + 1)):
    #Moultiple colums.
    for j in range(1,(n + 1)):
        print("*",end=" ")
    print()