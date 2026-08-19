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

num = int(input("Enter a value: "))

res = recursive_CountDigits(num,0)
print("The count of numbers are: ",res)

print()

pow = recursive_CountDigits(num,0)
if recursive_ASN:
    print("The",num,"is an Arm-Strong Number.")
else:
    print("The",num,"is not an Arm-Strong Number.")