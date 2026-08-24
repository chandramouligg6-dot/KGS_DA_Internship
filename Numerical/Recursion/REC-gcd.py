# WAP to display the GCD of two number using recursion (Eculidian Algorithm).

def ecuGCD(n1,n2):
    if n1 == 0:
        return n2
    if n1 < n2:
        n1, n2 = n2, n1
    return ecuGCD((n1 % n2), n2)

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

res = ecuGCD(num1,num2)
print(res)



def recGCD(n1, n2):
    if n2 == 0:
        return n1
    return recGCD(n2, n1 % n2)

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

result = recGCD(n1, n2)
print(result)