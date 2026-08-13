#WAP to check whether the given number is a prime number or not.

def Factors(n):
    i=1
    while i*i<=n:
        if n % i == 0:
            print(i,end=" ")
            if i != n//i:
                print((n//i),end=" ")
        i+=1
        
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

def isPrime(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count ==2 

num = int(input("Enter the number "))

print("The factors of", num, "are:",end=" ")
Factors(num)
print()

print("The number of factors of ",num, "is: ",countFactors(num))

print("The number of cycles taken to get all the factors of" ,num,"is: ",countFactorsCycles(num))

if isPrime(num):
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")