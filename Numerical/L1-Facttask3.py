#WAP to count the number of cycles taken to get all the factors of a given number.

def countFactorCycles(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Example usage
num = int(input("Enter a number: "))
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorCycles(num)}")