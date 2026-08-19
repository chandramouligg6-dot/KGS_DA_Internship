# Interger Palindrome of a number with recursion 

def intPalindromeNum(n, rev,temp):
    if n <= 0:
        return rev == temp
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
    return intPalindromeNum(n,rev,temp)

num = int(input("Enter the number: "))
flag = intPalindromeNum(num,0,num)
if flag:
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")