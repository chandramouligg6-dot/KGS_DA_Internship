# WAP for first n natural palindrome numbers and non palindrome also


def isPalindrome(n):
    temp = n
    
    if n < 0:
        n = n * (-1)
    rev = 0
    
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n //10
        
    if temp < 0:
        rev = rev *(-1)
    
    return temp == rev

n = int(input("Enter a natural number to check if it is a palindrome: "))
print(f"\nThe number {n} is a palindrome:")
print()
print("Palindrome Numbers are:")
for i in range(1, n + 1):
    if isPalindrome(i):
        print(i,end="," )
print()
print("\nNON Palindrome Numbers are:")
for i in range(1, n + 1):
    if not isPalindrome(i):
        print(i,end="," )

