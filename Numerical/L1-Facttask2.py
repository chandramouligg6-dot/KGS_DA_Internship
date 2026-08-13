#WAP to count all the factors of a given number.

def countFactors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

num = int(input("Enter a number: "))
print(f"The number of factors of {num} is: {countFactors(num)}")