#Email Validator

email = input("Enter you email address:")

at_index = email.find('@')
dot_index = email.rfind('.')

username = email[ : at_index]
domain = email[at_index + 1: dot_index]
extension = email[dot_index + 1:]
reversed_email = email[::-1]

print("The username: ",username)
print("The domain is: ",domain)
print("The extension of mail is: ",extension)
print("The reverse of mail is: ",reversed_email)