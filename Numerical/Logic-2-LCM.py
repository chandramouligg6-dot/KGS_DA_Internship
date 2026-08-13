# # WAP t oprint an LCM of two numbers with custmised function.

def LCMLogic2(n1,n2):
    lcm = n1
    if n2 > n1:
        lcm = n2
    while n1 *n2 != lcm:
        if lcm % n1 == 0 and lcm % n2 ==0:
            break
        lcm +=1
    return lcm

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

result2 = LCMLogic2(n1,n2)
print("The LCM of Two numbers of Logic2: ",result2)