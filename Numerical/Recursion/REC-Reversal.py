# WAP to display the reversal of number for a given number using recursion.

def recRev(n, rev):
    if n <= 0:
        return rev
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
    return recRev(n,rev)

num = int(input("Enter the number: "))
result = recRev(num,0)
print("The Reversal of numbers are: ",result)