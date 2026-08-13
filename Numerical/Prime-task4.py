#​WAP to display first "n" Prime Num's and first "n" Non Prime Num's.

def isPrime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n % i==0:
            return False
    return True

n = int(input("Enter the number of prime and non-prime numbers to display: "))
prime_count = 0
non_prime_count = 0
num = 2

print(f"First {n} prime numbers are:")
while prime_count < n:
    if isPrime(num):
        print(num, end=" ")
        prime_count += 1
    num += 1

print(f"\nFirst {n} non-prime numbers are:")
num = 2
while non_prime_count < n:
    if not isPrime(num):
        print(num, end=" ")
        non_prime_count += 1
    num += 1
