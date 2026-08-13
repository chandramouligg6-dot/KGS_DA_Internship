def countFactors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

def countFactorsCycles(n):
    count = 0
    i = 1
    while i * i <= n:
        count += 1  
        if n % i == 0:
            count += 1  
            if i != n // i:
                count += 1  
        i += 1
    return count

def isprime(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count==2

num = int(input("Enter a number: "))
print(f"The number of factors of {num} is: {countFactors(num)}")

print(f"The number of cycles taken to get all the factors of {num} is: {countFactorsCycles(num)}")

res = isprime(num)
print("The number of factors and prime number are: ")
if res:
    print("The number is prime number")
else:
    print("The number is not a prime number ")