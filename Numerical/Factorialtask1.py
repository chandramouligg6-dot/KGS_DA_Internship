# WAP to display the factorial of a given number using a customised function.

def Factorial(n):
    fact=1
    
    for i in range(2,n+1):
        fact *=i
    return fact

num=int(input("Enter the number"))
res=Factorial(num)
print("The factorial of a number is:",res)
