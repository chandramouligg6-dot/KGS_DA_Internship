# WAP to display the fibonacci number using recursion.

def findFibonacci(pos, n1, n2):
    if pos <= 0:
        return
    print(n1,end=" ")
    findFibonacci((pos-1), n2, (n1+n2))

pos = int(input("Enter a number: "))
findFibonacci(pos,0,1) 