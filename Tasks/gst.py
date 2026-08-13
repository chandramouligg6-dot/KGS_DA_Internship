print("=========GST CALCULATOR=========")

price=int(input("Enter the price of product: "))
gst_percentage=int(input("Enter the GST Percentage: "))

def gst_calculator(price,gst_percentage):
    amt = price + gst_percentage
    calculation =  (price*gst_percentage)/100
    final_amt = calculation + price
    return final_amt
    
print("Final Amount: ",gst_calculator(price,gst_percentage))