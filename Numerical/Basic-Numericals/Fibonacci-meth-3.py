#WAP display the fibonacci series up to n terms using a customised function with DECREMENT "FOR" LOOP.

def fibonacci(pos):
    n1 = 0
    n2 = 1
    
    for i in range(pos, 1-1, -1):
        print(n1, end=' ')
        temp = n1 + n2
        n1 = n2
        n2 = temp

num = int(input("Enter the number of terms: "))
fibonacci(num)