# WAP to find the count of digits 

def countDigits(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

num = int(input("Enter the Digits to count: "))
print("The count of digits of",num,"is: ",countDigits(num))