TOTAL_STUDENTS = 10

total_marks = 0
highest_marks = 0
lowest_marks = 100

pass_count = 0
fail_count = 0
distinction_count = 0
first_class_count = 0
second_class_count = 0

print("=== ONLINE EXAM MARK ENTRY ===")

for i in range(1, TOTAL_STUDENTS + 1):
    print("Enter marks for Student", i, "(0-100):")
    marks = float(input())
    
    while marks > 100 or marks < 10:
        print("Please reentry marks correctly (0-100):")
        marks = float(input())

    total_marks = total_marks + marks
    
    if marks > highest_marks:
        highest_marks = marks
        
    if marks < lowest_marks:
        lowest_marks = marks
    
    # Determine immediate result and category counts
    if marks >= 75:
        result = "Pass - Distinction"
        pass_count = pass_count + 1
        distinction_count = distinction_count + 1
    elif marks >= 60:
        result = "Pass - First Class"
        pass_count = pass_count + 1
        first_class_count = first_class_count + 1
    elif marks >= 35:
        result = "Pass - Second Class"
        pass_count = pass_count + 1
        second_class_count = second_class_count + 1
    else:
        result = "Fail"
        fail_count = fail_count + 1
        
    print("--> Immediate Result for Student", i, ":", result)
    print("")

# Calculate average
avg_marks = total_marks / TOTAL_STUDENTS

# Display Final Report
print("===================================")
print("          FINAL REPORT          ")
print("===================================")
print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("-----------------------------------")
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)
print("Distinction Count:", distinction_count)
print("First Class Count:", first_class_count)
print("Second Class Count:", second_class_count)
print("===================================")