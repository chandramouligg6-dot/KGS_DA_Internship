# WAP for fatorial of number with recursion

def recFactorial(n):
    if n <= 1:
        return 1
    return n* recFactorial(n-1)

num = int(input("Enter a value: "))
result = recFactorial(num)
print("The Factorial of",num,"is: ",result)