# Recursive function for counting the numbers 

def recursiveCountDigits(n,count):
    if n<=0:
        return count
    n = n // 10 
    count = count + 1
    return recursiveCountDigits(n,count)

n = int(input("Enter the number: "))
result = recursiveCountDigits(n,0)
print("The count of numbers are: ",result)




# Method-2 with code optimiziation

def recursive_CountDigits(n,count):
    if n<=0:
        return count
    return recursive_CountDigits(n//10,count + 1)

num = int(input("Enter the number: "))
res = recursive_CountDigits(num,0)
print("The count of numbers are: ",res)