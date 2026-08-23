#WAP to display all the Prime Num's present in a user defined range.Version 2

def Factors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            print(i, end=" ")
            if i != n // i:
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

def isPrime(n):
    if n < 2:
        return False
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count == 2


start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("=" * 50)

for num in range(start, end + 1):
    print(f"\n--- Analysis for Number: {num} ---")

    print("Factors:", end=" ")
    Factors(num)
    print()

    print("Number of factors:", countFactors(num))
    print("Cycles taken:", countFactorsCycles(num))

    if isPrime(num):
        print("Status: PRIME")
    else:
        print("Status: NOT PRIME")

print("=" * 50)