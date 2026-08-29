# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1 


n = int(input("Enter a value: "))

for i in range(n, 0,-1):
    for j in range(n,i-1,-1):
        print(i,end=" ")
    print()







# 1 2 3 4 
# 2 3 4 
# 3 4 
# 4

n = int(input("Enter a value: "))
for i in range (1, n + 1):
    for j in range(i, n + 1):
        print(j,end=" ")
    print()







# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

n = int(input("Enter a value: "))
noc = 1
for i in range(1,n*2):
    for j in range(1,noc+1):
        print(j,end=" ")
    print()
    if i < n:
        noc+=1
    else:
        noc-=1







# 4 
# 3 4 
# 2 3 4 
# 1 2 3 4 
# 2 3 4 
# 3 4 
# 4

n = int(input("Enter a value: "))
noc = n

for i in range(1, n * 2):
    for j in range(noc, n + 1):
        print(j, end=" ")
    print()

    if i < n:
        noc -= 1
    else:
        noc += 1






# 1 2 3 4 
# 2 3 4 5 
# 3 4 5 6 
# 4 5 6 7

# task-1

n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(i, i + n):
        print(j, end=" ")
    print()





# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 

#Task-2

n = int(input("Enter a value: "))
noc = n

for i in range(1, n * 2):
    for j in range(1, noc + 1):
        print(j,end=" ")
    print()

    if i < n:
        noc -= 1
    else:
        noc += 1






# 1 2 3 4 
# 2 3 4 
# 3 4 
# 4 
# 3 4 
# 2 3 4 
# 1 2 3 4

n = int(input("Enter a value: "))
noc = 1

for i in range(1, n * 2):
    for j in range(noc, n + 1):
        print(j, end=" ")
    print()

    if i < n:
        noc += 1
    else:
        noc -= 1






# 1 2 3 4 
#   2 3 4 
#     3 4 
#       4 
#     3 4 
#   2 3 4 
# 1 2 3 4


n = int(input("Enter a value: "))
noc = 1

for i in range(1, n * 2):
    for k in range(1, noc):
        print(" ", end=" ")

    for j in range(noc, n + 1):
        print(j, end=" ")
    print()

    if i < n:
        noc += 1
    else:
        noc -= 1





# 1 2 3 4 
#  2 3 4 
#   3 4 
#    4 
#   3 4 
#  2 3 4 
# 1 2 3 4

n = int(input("Enter a value: "))
noc = 1

for i in range(1, n * 2):
    for k in range(1, noc):
        print(" ", end="")

    for j in range(noc, n + 1):
        print(j, end=" ")
    print()

    if i < n:
        noc += 1
    else:
        noc -= 1






# 1 2 3 4 
# 2 2 3 4 
# 3 3 3 4 
# 4 4 4 4

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i < j:
            print(j,end=" ")
        else:
            print(i, end=" ")
    print()





# 4 4 4 4 
# 4 3 3 3 
# 4 3 2 2 
# 4 3 2 1 


n = int(input("Enter a value: "))
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if i > j:
            print(i,end=" ")
        else:
            print(j, end=" ")
    print()





# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1

# pascal Triangle

n = int(input("Enter a value:"))
for i in range(0, n):
    num = 1
    for j in range(0, i + 1):
        print(num,end=" ")
        num = num * (i-j) // (j +1)
    print()






#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# pascal Triangle

n = int(input("Enter a value:"))
for i in range(0, n):
    num = 1
    for k in range(n, i, -1):
        print(" ",end="")
    for j in range(0, i + 1):
        print(num,end=" ")
        num = num * (i-j) // (j +1)
    print()






# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16 

n = int(input("Enter a value: "))

num = 1
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(num, end=" ")
        num += 1
    print()







# 1 2 3 4 
# 8 7 6 5 
# 9 10 11 12 
# 16 15 14 13 

n = int(input("Enter a Value: "))

count1 = 1
for i in range(1, n + 1):
    for j in range(1, n +  1):
        if i % 2 != 0:
            print(count1,end=" ")
            count2 = count1
        else:
            print(count2,end=" ")
            count2 -= 1
        count1 += 1
    print()
    count2 = count2 + n


# Version-2

n = int(input("Enter a Value: "))

count1 = 1
for i in range(1, n + 1):
    if i % 2 == 0:
        count2 = count1 + n - 1
    for j in range(1, n + 1):
        if i % 2 != 0:
            print(count1, end=" ")
        else:
            print(count2, end=" ")
            count2 -= 1
        count1 += 1
    print()





# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 

n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if (i+j) % 2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()





# 1
# 1 0 
# 1 0 1
# 1 0 1 0

n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j % 2 != 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()




# 1 0 1 0
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1

n = int(input("Enter a value: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2==0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()




# 1 1 1 1 
# 0 0 0
# 1 1
# 1 

n = int(input("Enter a value: "))

for i in range(n,0,-1):
    for j in range(i):
        if i % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()




# 0 1 0 1 
# 1 0 1
# 0 1
# 1

n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 2):
        if (i + j) % 2 != 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()



# 4 3 2 1
# 3 3 2 1
# 2 2 2 1
# 1 1 1 1

n = int(input("Enter a value: "))
for i in range (n, 0, -1):
    for j in range(n, 0, -1):
        if i<j:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
