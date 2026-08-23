#​ WAP to display first "n" Prime Num's and first "n" Non Prime Num's.

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

n = int(input("Enter the value of n: "))

print(f"\nThe first {n} Prime numbers are:")
prime_count = 0
current_num = 2
while prime_count < n:
    if isPrime(current_num):
        print(current_num, end=" ")
        prime_count += 1
    current_num += 1
print()

print(f"\nThe first {n} Non-Prime numbers are:")
non_prime_count = 0
current_num = 1
while non_prime_count < n:
    if not isPrime(current_num):
        print(current_num, end=" ")
        non_prime_count += 1
    current_num += 1
print()