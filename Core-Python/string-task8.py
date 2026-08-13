# Bank Account Masking

account_no = input("Enter you Bank account number: ") 

# print("*"* len(account_no[:-4])+account_no[-4:])

masked_account = "*" * len(account_no[:-4]) + account_no[-4:]

print("Original Account Number :", account_no)
print("Masked Account Number   :", masked_account)