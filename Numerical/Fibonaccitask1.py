# WAP display the fibonacci series up to n terms using a customised function with DECREMENT WHILE LOOP.

def fibonacci(pos):
    n1 = 0
    n2 = 1
    
    while pos > 0:
        print(n1, end=' ')
        temp = n1 + n2
        n1 = n2
        n2 = temp
        pos -= 1
        
pos = int(input("Enter the number of terms: "))
fibonacci(pos)