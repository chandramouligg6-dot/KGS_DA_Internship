# 9.	WAP to reverse an array.

def createIntarray():
    l1 = []
    while True:
        try:
            val = int(input("Enter a Value: "))
            l1.append(val)
        except Exception as e:
            return l1
            
# Logic-1 using 3rd Memory 

def ReverseArray1(arr):
    res = []
    for i in range(len(arr)-1,(0-1),-1):
        res.append(arr[i])
    return res

# Logic-2 without using 3rd variable 

def ReverseArray2(arr):
    i, j = 0, len(arr)-1
    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
    
print("Enter an array elements to be created: ")
arr = createIntarray()
print("The created array is:", arr)

res = ReverseArray1(arr)
print("The Reversed Array (Logic1): ", res)

res1 = ReverseArray2(arr)
print("The Reversed Array (Logic2) ", res1)