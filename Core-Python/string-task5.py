#Password Strength Checker

password = input("Enter the password: ")

first_char = password[0]
last_char = password[-1]

middle_chars = password[1:-1]

reversed_password = password[::-1]

password_length = len(password)

print("Original Password  :", password)
print("-----------------------------------")
print("First Character    :", first_char)
print("Last Character     :", last_char)
print("Middle Characters  :", middle_chars)
print("Reversed Password  :", reversed_password)
print("Password Length    :", password_length)