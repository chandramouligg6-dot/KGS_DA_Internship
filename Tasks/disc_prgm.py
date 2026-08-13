# WAL to implement discount based on the Final Purchase bill
bill_amt = float(input("\n Enter the Final Bill Amount: \n"))

discount_percentage = 0
discount_amt = (bill_amt * discount_percentage) / 100
final_bill_amt = bill_amt - discount_amt

print("")


if bill_amt >= 1000 and bill_amt < 5000:
    discount_percentage = 10
    print("........Congratulation You got 10% Discount on you Final Bill Amount........")
elif bill_amt >= 5000 and bill_amt <= 10000:
    discount_percentage = 15
    print("........Congratulation You got 15% Discount on you Final Bill Amount........")
elif bill_amt > 25000:
    discount_percentage = 25
    print("........Congratulation You got 25% Discount on you Final Bill Amount........")
else:
    discount_percentage = 0
    print("........NO DISCOUNT FOR YOU........")


print("\n----------Purchase Summary---------")
print("")
print("Purchased Bill Amt: ", bill_amt)
print("Discount Amount on your Bill: ", discount_amt)
print("Your Final Amount to Pay: ", final_bill_amt)