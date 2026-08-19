#WAP to count all the factors of a given number.

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

num = int(input("Enter a number: "))
print(f"The number of factors of {num} is: {countFactors(num)}")