# WAP to display the reversal of number for a given number using recursion.

def recRev(n, rev,temp):
    if n <= 0:
        return rev
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
    return recRev(n,rev,temp)

num = int(input("Enter the number: "))
result = recRev(num,0,num)
print("The Reversal of numbers are: ",result)