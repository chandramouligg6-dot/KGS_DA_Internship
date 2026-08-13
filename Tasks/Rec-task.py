# -	WAP to display the sum of the first “n” natural numbers.
	# N = 5  5+4+3+2+1 =15


def displaySum(n):
    if n == 0:
        return 0
    if n == 1:
        print(n, end=" = ")
    else:
        print(n, end="+")
    return n + displaySum(n - 1)

num = int(input("Enter a number: "))
total = displaySum(num)
print(total)

# WAP to sum all the digits present in a given number. 
	# N = 5481
	# N = 5481 	0+1
	# N = 548 	1+8
	# N = 54 	9+4
	# N = 5 		13+5
	# N = 0		ret 18

def sumDigits(n):
    if n == 0:
        return 0
    
    last_digit = n % 10
    remaining_number = n // 10

    return last_digit + sumDigits(remaining_number)

num = int(input("Enter a number: "))
print("Sum of digits:", sumDigits(num))