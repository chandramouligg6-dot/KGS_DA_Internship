def gcdecu(n1, n2):
    
    while n2 > 0:
        n1, n2 = n2, n1 % n2
    return n1

print("Enter two numbers to find their GCD:")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
res = gcdecu(n1, n2)
print(f"The GCD of {n1} and {n2} is {res}")