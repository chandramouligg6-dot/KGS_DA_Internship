def nth_Fibonacci(pos):

    if pos<=1:
        return pos
    return nth_Fibonacci(pos - 1) + nth_Fibonacci(pos - 2)

pos = int(input("Enter a num: "))
res = nth_Fibonacci(pos)
print("The value present in the position",pos,"is: ",res)