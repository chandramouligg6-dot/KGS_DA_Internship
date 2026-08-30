# WAP to reverse a number present in a user-defined range.

def isReverse(n):
    temp = n
    rev = 0
    
    if n < 0:
        n = n * (-1)
    
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
        
    if temp < 0:
        rev = rev * (-1)
    
    return rev

start = int(input("Enter the start of range: "))
end = int(input("Enter the end range: "))

print(f"\nThe reversed numbers in the range [{start}, {end}]:")
for i in range(start, end + 1):
    reversed_num = isReverse(i)
    print(reversed_num, end=" ")