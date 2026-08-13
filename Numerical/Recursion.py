# Write a Logic to display 4(n) to 1 in decrementing order, where no loops are allowed to be taken nor code redudency is allowed.

def displayNum4(n):
    print(n)
    displayNum3(n - 1)
    return
def displayNum3(n):
    print(n)
    displayNum2(n - 1)
    return
def displayNum2(n):
    print(n)
    displayNum1(n - 1)
    return
def displayNum1(n):
    print(n)
    return

num = int(input("Enter a number four: "))
displayNum4(num)

# To reduce the code redudency 

def displayNum(n):
    if n <= 0:
        return
    print(n)
    displayNum(n - 1)

num = int(input("Enter a number: "))
displayNum(num)

# I/p: 4 , O/p:43211234

def displayNum(n):
    if n <= 0:
        return
    print(n, end=" ")
    displayNum(n - 1)
    print(n, end=" ")  

num = int(input("Enter a number: "))
displayNum(num)
print()

# I/p: 4, O/p:12344321

def displayNum(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    displayNum(n, current + 1)
    print(current, end=" ") 

num = int(input("Enter a number: "))
displayNum(num)