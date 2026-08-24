# WAP to display LCM of given two numbers using recursion.

def findLCM(n1,n2,lcm):
    if n1*n2 == 0:
        return lcm
    
    if lcm % n1 == 0 and lcm % n2 == 0:
        return lcm
    
    return findLCM(n1,n2,(lcm+1))

n1 = int(input("Enter the first Number: "))
n2 = int(input("Enter the second Number: "))
lcm = n1
if n2 > n1:
    lcm = n2
res = findLCM(n1,n2,lcm)
print("The LCM of",n1,"and",n2,"is: ",res)  