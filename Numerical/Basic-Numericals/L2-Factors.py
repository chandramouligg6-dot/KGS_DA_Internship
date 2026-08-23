def Factors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            if i != (n // i):
                print((n // i), end=" ")
        i += 1

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
    cycles = 0
    i = 1
    while i * i <= n:
        cycles += 1 
        i += 1
    return cycles


num = int(input("Enter the number: "))
print("\nThe factors of", num, "are:", end=" ")
Factors(num)
print(f"\nThe number of factors of {num} is: {countFactors(num)}")
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorsCycles(num)}")