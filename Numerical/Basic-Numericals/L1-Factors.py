def displayFactors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ") 

num = int(input("Enter a number: "))
displayFactors(num)

def countFactors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count
print()
# num = int(input("Enter a number: "))
print(f"The number of factors of {num} is: {countFactors(num)}")

def countFactorCycles(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# # Example usage
# num = int(input("Enter a number: "))
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorCycles(num)}")