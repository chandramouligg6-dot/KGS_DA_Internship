# WAP to check whether a numbers are co - prime or not using a customised function.

def findGCD(a, b):
    hcf = 1
    lower = a
    if b > a:
        lower = b
    for i in range(2,(lower +1)):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = findGCD(num1, num2)

print("The GCD of", num1, "and", num2, "is", res)

if res == 1:
    print("The numbers", num1, "and", num2, "are co-prime.")
else:
    print("The numbers", num1, "and", num2, "are not co-prime.")