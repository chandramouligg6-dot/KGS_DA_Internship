# WAP to display a numbe is Happy or unHappy using recursion

def findHappy(n):
    if n == 1:
        return True
    
    elif n == 4:
        return False
    
    sum = 0 
    while n > 0:
        base = n % 10
        sum = sum + (base*base)
        n = n // 10

    return findHappy(sum)

n = int(input("Enter a number: "))
if findHappy(n):
    print("The number",n,"is a Happy number.")
else:
    print("The number",n,"is NOT a Happy number.")