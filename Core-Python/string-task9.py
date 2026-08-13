# Student Roll Number

roll_no = "AIML20260045"

department     = roll_no[:4]
admission_year = roll_no[4:8]
student_roll   = roll_no[8:]

print("Full Roll Number :", roll_no)
print("---------------------------------")
print("Department       :", department)
print("Admission Year   :", admission_year)
print("Roll Number      :", student_roll)