#​WAP to count the num of cycles taken to get all the factors of a given number.

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

num = int(input("Enter a number: "))
print(f"The number of cycles taken to get all the factors of {num} is: {countFactorsCycles(num)}")