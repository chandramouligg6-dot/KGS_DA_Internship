# WAP for palandrome with custmized function with user defined range.

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

start  = int(input("Enter start range: "))
end = int(input("Enter end range: "))
print(f"\nThe Palandrome numbers in the range [{start}, {end}]:")

for i in range(start, end + 1):
    res = isPalindrome(i)
    if res:
        print(f"{i} is a Palindrome number.")
    else:
        print(f"{i} is not a Palindrome number.")