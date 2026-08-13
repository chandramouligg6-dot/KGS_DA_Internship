# Website URL Analyzer

url = "https://www.google.com"

colon_index = url.find(":")
dot_1 = url.find(".")
dot_2 = url.rfind(".")

protocol     = url[:colon_index]
website_name = url[dot_1 + 1 : dot_2]
extension    = url[dot_2 + 1 :]

print("Full URL      :", url)
print("----------------------------")
print("Protocol      :", protocol)
print("Website Name  :", website_name)
print("Extension     :", extension)