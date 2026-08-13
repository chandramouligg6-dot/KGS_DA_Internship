#All the factors of a given number can be listed within the range of 1 to the direct square root of the number or the lower nearest square root of the given number.
# wap a display all the factores of a given number

def Factors(n):
    i=1
    while i*i<=n:
        if n % i == 0:
            print(i,end=" ")
            if i != (n//i):
                print((n//i),end=" ")
        i+=1
        
num=int(input("Enter the number "))
print("The factors of", num, "are:",Factors(num),end=" ")
