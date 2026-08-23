# WAP to print an LCM of two numbers with custmised function.

def LCMLogic1(n1,n2):
    lcm = n1
    if n2 > n1:
        lcm = n2
    while True:
        if lcm % n1 == 0 and lcm % n2 ==0:
            return lcm
        lcm += 1

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

result = LCMLogic1(n1,n2)
print("The LCM of Two numbers of Logic1: ",result)