# WAP for Factors with recursion

def recFactors(n,i):
    if i > n:
        return
    if n % i == 0:
        print(i,end=" ")
    recFactors(n,(i+1))

num = int(input("Enter a number: "))
recFactors(num,1)