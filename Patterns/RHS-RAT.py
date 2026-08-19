# RHS Right-angle Triangle.

n = int(input("Enter a value: "))

#outer loop for ROWS
for i in range(1, (n + 1)):
    #INNER LOOP IS MAINLY FOR COLUMS 
    #Inner-1 loop is for SPACE
    for k in range(n, i, -1):
        print(" ",end= "")

    #Inner-2 loop is for STAR
    for j in range(1, (i + 1)):
        print("*",end= "")
    print()