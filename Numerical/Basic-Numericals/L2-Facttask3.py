#​WAP to count the num of cycles taken to get all the factors of a given number.

def countFactorsCycles(n):
    cycles = 0
    i = 1
    while i * i <= n:
        cycles += 1 
        i += 1
    return cycles

num = int(input("Enter a number: "))
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorsCycles(num)}")