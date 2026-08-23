#WAP to display the first “n” natural numbers in reverse order.

def isReverse(n):
    temp = n
    
    if n < 0:
        n = n * (-1)
    rev = 0
    
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
        
    if temp < 0:
        rev = rev * (-1)
    
    return rev
    
n = int(input("Enter how many natural numbers: "))
print(f"\nThe first {n} natural numbers in reverse order:")

for i in range(1, n + 1):
    reversed_num = isReverse(i)
    print(reversed_num,end=" ")