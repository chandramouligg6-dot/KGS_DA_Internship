# WAP for palandrome with custmized function.

def isPalindrome(n):
    temp = n
    rev = 0

    if n < 0:
        n = n * (-1)

    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n //10
        
    if temp < 0:
        rev = rev *(-1)
        
    return temp == rev

num  = int(input("Enter a number: "))
res = isPalindrome(num)

if res:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")