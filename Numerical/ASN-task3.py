#WAP to display first "n" ASN's

def countDigits(n):
    count = 0 
    while n > 0:
        n = n // 10
        count += 1
    return count  
def isASN(n):
    temp = n  
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

n = int(input("Enter how many Arm Strong Numbers You want: "))
print(f"The first {n} Arm Strong Numbers are: ")        
count = 0 
num = 0 
while count < n:
    if isASN(num):
        print(num,end=" ")
        count +=1
    num +=1
