# Reveresal of number in recursion 

def reverseNum(n, rev):
    if n <= 0:
        return rev
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
    return reverseNum(n,rev)

num = int(input("Enter the number: "))
result = reverseNum(num, 0)
print("The reversal of",num,"is",result)