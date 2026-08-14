# WAP to find the count of digits with user defined range

def countDigits(n):
    count = 0
    if n<0:
        return count
    while n > 0:
        n = n // 10
        count += 1
    return count

start = int(input("Enter the start of range: "))
end = int(input("Enter the end range: "))
number = 0
for i in range(start, end + 1):
    number += 1

print(f"start = {start}, end = {end} the count of digits is {number}")
