# WAP to display the factors and count of factors for a given number using recursion.

def Factor(n,i):
    if  i * i>n:
        return Factor
    if n % i == 0:
        print(i,end=" ")
        if i != (n//i):
            print(n//i,end=" ")
    return Factor(n,(i+1))

def CountFactor(n,i,Count):
    if i * i > n:
        return Count
    if n % i == 0:
        Count +=1
        if i != (n//i):
            Count +=1
    return CountFactor(n,(i+1),Count)

num=int(input("enter the number: "))

print("The factors of",num,"are: ")
Factor(num,1)

res=CountFactor(num,1,0)
print("\nThe number of factors in",num,"is:",res)