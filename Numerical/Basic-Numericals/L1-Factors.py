# WAP to display a factors of given number, count of factors and factors cycles with logic-1 using custmised function.

def displayFactors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ") 

def countFactors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def countFactorCycles(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count


num = int(input("Enter a number: "))
displayFactors(num)
print(f"\nThe number of factors of {num} is: {countFactors(num)}")
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorCycles(num)}")