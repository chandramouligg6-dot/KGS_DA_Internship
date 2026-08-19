# WAP to check whether the given number is an ASN or not using a customised function.

def countDigits(n):
    count = 0 
    while n > 0:
        n = n // 10
        count += 1
    return count  

def isASN(n):
    temp = n
    pow = 0
    asn = countDigits(n)
    
    if n < 0 :
        n = n * (-1)
    
    while n >0:
        base = n % 10
        asn = asn + (base**pow)
        n = n // 10

    if temp < 0 :
        asn = asn * (-1)

    return temp ==asn

num = int(input("Enter a Number:"))
if isASN(num):
    print("The number",num,"is an Arm Strong Number.")
else:
    print("The number",num,"is not an Arm Strong Number.")