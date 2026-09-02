#      a 
#     b c 
#   c d e 
# d e f g 
#   c d e 
#     b c 
#       a


n = int(input("enter the number: "))
noc = 1

for i in range(1, n * 2):
    for k in range(n - noc):
        print(" ", end=" ")
    for j in range(noc, noc * 2):
        print(chr(96 + j), end=" ")
        
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1








#  a 
#   b c 
#  c d e 
# d e f g 
#  c d e 
#   b c 
#    a



n = int(input("enter the number: "))
noc = 1

for i in range(1, n * 2):
    for k in range(n - noc):
        print(" ", end="")
    for j in range(noc, noc * 2):
        print(chr(96 + j), end=" ")
        
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1







# a a a a 
# b   b 
# c c 
# d 
# c c 
# b   b 
# a a a a




n = int(input("Enter a value: "))

noc = 1
for i in range(1, n  * 2):
    for j in range(noc, n + 1):
        if j == noc or i == 1 or i == (n * 2) - 1 or j == n:
            print(chr(96 + noc),end=" ")
        else:
            print(" ",end=" ")
    print()
    if i < n:
        noc += 1
    else:
        noc -= 1








# 1 2 3 4 3 2 1 
# 1 2 3 2 1 
# 1 2 1 
# 1








n = int(input("Enter a Value: "))

for i in range(n, 0, -1):
    count = 1
    for j in range(1, i * 2):
        print(count,end=" ")
        if j < i:
            count += 1
        else:
            count -= 1
    print()






# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1




n = int(input("Enter a Value: "))

for i in range(1, n + 1):
    count = 1
    for j in range(1, i * 2):
        print(count,end=" ")
        if j < i:
            count += 1
        else:
            count -= 1
    print()











# A B C D C B A 
# A B C   C B A 
# A B       B A 
# A           A 







n = int(input("Enter a value: "))

noc = n
for i in range(1, n + 1):
    count = 1
    for j in range(1, n * 2):
        if j <= noc or j >= ((n * 2) - noc):
            print(chr(64 + count), end=" ")
        else:
            print(" ", end=" ")
        if j < n:
            count += 1
        else:
            count -= 1
    print()
    noc -= 1