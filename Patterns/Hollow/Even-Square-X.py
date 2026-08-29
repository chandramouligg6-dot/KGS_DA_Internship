# Logic Building for interview
# Even number Hollow Square

n = int(input("Enter a value: "))

if n % 2 == 0:
    n = n + 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == n or i == j or i == n or i == 1 or (i + j) == (n + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()