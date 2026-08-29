# Version 3

class Employee:
    company_name = "Health-Link"
    employee_count = 1000

    def __init__(self, employee_name, department):
        self.employee_name = employee_name
        self.department = department

    def generate_employee_id(self):
        Employee.employee_count += 1
        employee_id = "EMP" + "HLS" + str(Employee.employee_count)
        return employee_id

    def display_details(self, index):
        emp_id = self.generate_employee_id()
        print(f"\n--- Employee #{index} ---")
        print(f"Company Name         : {Employee.company_name}")
        print(f"Employee Name        : {self.employee_name}")
        print(f"Department           : {self.department}")
        print(f"Generated Employee ID: {emp_id}")
        print("-" * 40)

print("=" * 50)
print("WELCOME TO EMPLOYEE REGISTRATION SYSTEM")
print("=" * 50)

num_employees = int(input("\nHow many employee details do you want to add? "))

while num_employees <= 0:
    print("Please enter a positive number!")
    num_employees = int(input("\nHow many employee details do you want to add? "))

print(f"\nGreat! You are adding {num_employees} employee(s).")
print("-" * 50)

for i in range(num_employees):
    print(f"\n--- Entering details for Employee {i+1} of {num_employees} ---")
    name = input("Enter Employee Name: ")
    dept = input("Enter Department: ")
    
    emp = Employee(name, dept)
    emp.display_details(i+1)

# Summary
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(f"Total Employees Added: {num_employees}")
print(f"Total Employees in System: {Employee.employee_count - 1000}")
print(f"Company: {Employee.company_name}")
print("=" * 50)