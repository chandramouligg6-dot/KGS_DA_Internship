#WAP to display all the Prime Num's present in a user defined range.

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


# Taking user input for the range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"\nPrime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if isPrime(num):
        print(num, end=" ")

print()  