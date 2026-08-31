#1) str = "R A M A "
str = "R A M A "
result = " "
for char in str:
    if char != " ":
        result += char
print("Original String is: ",str)
print("New sting is: ",result)
print("="*50)

# 2) I/p = Rama
#    O/p = amaR
str1 = "lewis"
result1 = " "
for i in str1:
    result1 = i + result1
print("Original string is: ",str1)
print("Reversed string is: ",result1)
print("="*50)

# 3) I/p = "Kaizentrix globaal solutions"
#    O/p = "solutions globaal Kaizentrix"

s1 = "Kaizentrix globaal solutions"
s2 = s1.split()
print(s2)
print(len(s2))
new = ""
for i in s2:
    new = i + " " + new
print(new)
print("="*50)

# 4) I/p = "Hello"
#    O/p = "Helo"

input_str = "Hello"
res = ""

for char in input_str:
    if char not in res:
        res += char
print(res)

# 5) I/p = "Rama is sleeping and Rama is snooring"
#    O/p = "Rama is sleeping and snooring"

string1 = "Rama is sleeping and Rama is snooring"
words = string1.split()
print(len(words))
seen_words = " "

for word in words:
    seen_words = seen_words + " "+ word

print("Original string:", string1)
print("Output string:  ", seen_words)