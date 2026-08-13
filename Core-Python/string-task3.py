#Aadhaar Number Formatter

num_str = input("Enter 12-digit number: ")

first_4 = num_str[:4]
middle_4 = num_str[4:8]
last_4 = num_str[8:]

print("\nFirst 4 digits  :", first_4)
print("Middle 4 digits :", middle_4)
print("Last 4 digits   :", last_4)

print(first_4,middle_4,last_4)