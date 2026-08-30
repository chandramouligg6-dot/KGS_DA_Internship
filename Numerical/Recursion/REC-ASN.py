# WAP for Armstrong numbers with recursion

def recursive_CountDigits(n,count):
    if n<=0:
        return count
    return recursive_CountDigits(n//10,count + 1)

def recursive_ASN(n, asn, pow, temp):
    if n <= 0:
        return asn == temp
    base = n % 10
    asn = asn + (base**pow)
    n = n // 10
    return recursive_ASN(n, asn, pow, temp)
num = int(input("Enter a value: "))

pow = recursive_CountDigits(num,0)
print("The count of numbers are: ",pow)

print()

if recursive_ASN(num, 0, pow, num):
    print("The",num,"is an Arm-Strong Number.")
else:
    print("The",num,"is not an Arm-Strong Number.")