#Username Generator

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

username = f"{first_name.lower()}.{last_name.lower()}"

initials = (first_name[0] + last_name[0]).upper()

print("\nGenerated Details:")
print("------------------")
print("Username :", username)
print("Initials :", initials)