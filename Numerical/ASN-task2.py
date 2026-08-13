# WAP to display all the ASN present in a user defined range.

def countDigits(n):
    n = abs(n)
    count = 0 
    while n > 0:
        n = n // 10
        count += 1
    return count  
def isASN(n):
    temp = abs(n)    
    if n < 0 :
        n = n * (-1)
    asn,pow = 0,countDigits(n)
    while n >0:
        base = n % 10
        asn = asn +(base**pow)
        n = n//10
    if temp < 0 :
       asn = asn * (-1)
    return temp ==asn
start = int(input("Enter the start of range: "))
end = int(input("Enter the end range: "))
print(f"The Arm Strong Number between {start} and {end}: ")
for num in range(start,end +1):
    if isASN(num):
        print(num,end=" ")
print(f"\nThe NON Arm Strong Number between {start} and {end}:")
for num in range(start,end +1):
    if not isASN(num):
        print(num,end=" ")
        