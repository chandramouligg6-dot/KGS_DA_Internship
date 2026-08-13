#WAP display the fibonacci series up to n terms using a customised function with INCREMENT "FOR" LOOP.

def fibonacci(pos):
    n1 = 0
    n2 = 1
    
    for i in range(1, pos + 1):
        print(n1, end=' ')
        temp = n1 + n2
        n1 = n2
        n2 = temp

pos = int(input("Enter the number of terms: "))
print("\nThe fibonacci series are", pos, "terms is displayed below.")
fibonacci(pos)


