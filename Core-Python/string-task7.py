#Vehicle Registration Number


reg_no = input("Enter Vehicle Registration Number (AB12DE1234): ")

state_code = reg_no[:2]
rto_code   = reg_no[2:4]
series     = reg_no[4:6]
veh_number = reg_no[6:]

# 3. Display Output
print("Vehicle Number    :", reg_no)
print("----------------------------")
print("State Code        :", state_code)
print("RTO Code          :", rto_code)
print("Series            :", series)
print("Vehicle Number    :", veh_number)