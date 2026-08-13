#1.	WAP to display all the factors of a given number.

def displayFactors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ") # Move to the next line

num = int(input("Enter a number: "))
displayFactors(num)