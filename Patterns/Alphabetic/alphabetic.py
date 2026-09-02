# a 
# b b 
# c c c 
# d d d d

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(96 + i),end=" ")
    print()




# D C B A 
# D C B 
# D C 
# D

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(n, (i - 1), -1):
        print(chr(64 + j),end=" ")
    print()

n = int(input("Enter a value: "))
for i in range(1, n + 1):
    for j in range(n, (i - 1), -1):
        print()






# a b c d e f 
# g h i j k l 
# m n o p q r 
# s t u v w x 
# y z a b c d 
# e f g h i j 


n = int(input("Enter a value: "))

value = 97
for i in range(n):
    for j in range(n):
        print(chr(value),end=" ")
        value += 1
        if value > 122:
            value = 97
    print()





# a b c d e f g h i 
# j k l m n o p q r 
# s t u v w x y z A 
# B C D E F G H I J 
# K L M N O P Q R S 
# T U V W X Y Z a b 
# c d e f g h i j k 
# l m n o p q r s t 
# u v w x y z A B C


n = int(input("Enter a value: "))

value = 97
count = 65
for i in range(1,n+1):
    for j in range(1,n+1):
        if value <= 122:
            print(chr(value),end=" ")
            value += 1
            if value > 122:
                count = 65
        else:
            print(chr(count),end=" ")
            count += 1
            if count > 90:
                value = 97
    print()







# A B C D E 
# B C D E 
# C D E 
# D E 
# E 


n = int(input("Enter a value: "))
for i in range (1, n + 1):
    for j in range(i, n + 1):
        print(chr(64+j),end=" ")
    print()




# D C B A 
# d c b a 
# D C B A 
# d c b a


n = int(input("Enter a value: "))


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 == 0:
            print(chr(101 - j),end=" ")
        else:
            print(chr(69 - j),end=" ")
    print()






# A B C D 
# d c b a 
# A B C D 
# d c b a


n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 != 0:
            print(chr(64 + j),end= " ")
        else:
            print(chr(101 - j),end=" ")
    print()







# d d d d 
# d c c c 
# d c b b 
# d c b a


n = int(input("Enter a value: "))

for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j >= i:
            print(chr(96 + j), end=" ")
        else:
            print(chr(96 + i), end=" ")
    print()







# d c b a 
# c c b a 
# b b b a 
# a a a a



n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= j:
            print(chr(96 + n - i + 1), end=" ")
        else:
            print(chr(96 + n - j + 1), end=" ")
    print()






# A b C d 
# a B c D 
# A b C d 
# a B c D



n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 ==0:
            print(chr(64 + j),end=" ")
        else:
            print(chr(96 + j),end=" ")
    print()






# A B C D 
# B B C D 
# C C C D 
# D D D D


n = int(input("Enter a value: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i <= j:
            print(chr(64 + j), end=" ")
        else:
            print(chr(64 + i), end=" ")
    print()






