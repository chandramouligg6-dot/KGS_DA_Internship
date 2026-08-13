# WAP to find the GCD of two numbers using a customised function.

def findGCD(n1, n2):
    hcf = 1
    lower = n1

    if n2 > n1:
        lower = n2

    for i in range(2,(lower +1)):
        if (n1 % i == 0 and n2 % i == 0):
            hcf = i
            
    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = findGCD(num1, num2)
print("The GCD of", num1, "and", num2, "is", res)