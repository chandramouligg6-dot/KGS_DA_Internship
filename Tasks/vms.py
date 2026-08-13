class VisitorManagementSystem:
    company_name = "KAIZENTRIX GLOBAL SOLUTIONS PVT LTD"
    title = "Corporate Visitor Management System"

    def __init__(self):
        self.visitor_Id = ""
        self.visitor_name = ""
        self.visitor_email = ""
        self.phone_number = ""
        self.person_to_meet = ""
        self.Department = ""
        self.purpose_of_visit = ""
        self.entry_time = 0
        self.exit_time = 0

    def display_menu(self):
        print("===========================================================")
        print(f"              {VisitorManagementSystem.company_name}"                         )
        print(f"              {VisitorManagementSystem.title}"                                )
        print("===========================================================")
        print("1. Visitor Check-in.")
        print("2. Visitor Check-out.")
        print("3. Visitor Guidance.")
        print("4. Exit.")

    def check_in(self):
        print("\n=========================VISITOR CHECK-IN ===========================\n")
        self.visitor_Id = input("Enter Visitor ID: ")
        self.visitor_name = input("Enter Visitor Name: ")
        self.visitor_email = input("Enter Visitor Email: ")
        self.company_name = input("Enter Company Name: ")
        self.phone_number = input("Enter Phone Number: ")
        self.person_to_meet = input("Enter Person to Meet: ")
        self.Department = input("Enter Department: ")
        self.purpose_of_visit = input("Enter Purpose of Visit: ")
        self.entry_time = int(input("Enter Entry Time (0 - 23): "))
        print("\nVisitor Check-in Successful!\n")

    def check_out(self):
        print("\n=========================VISITOR CHECK-OUT ===========================\n")

        self.exit_time = int(input("Enter Exit Time (0 - 23): "))
        duration = self.exit_time - self.entry_time

        print("\n========================VISITOR SUMMARY =============================\n")
        print(f"Visitor ID: {self.visitor_Id}")
        print(f"Visitor Name: {self.visitor_name}")
        print(f"Visitor Email: {self.visitor_email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Person to Meet: {self.person_to_meet}")
        print(f"Department: {self.Department}")
        print(f"Purpose of Visit: {self.purpose_of_visit}")
        print(f"Entry Time: {self.entry_time}")
        print(f"Exit Time: {self.exit_time}\n")
        print(f"Status: Visitor Check-out Successful! Duration of Visit: {duration} hours.")
        print("\nThank You for Visiting KAIZENTRIX GLOBAL SOLUTIONS PVT LTD. We hope you had a pleasant experience!\n")
        print("Visit Again! We look forward to welcoming you back soon!\n")

    def visitor_guidance(self):
        
        print("\n=========================VISITOR GUIDANCE ============================\n")
        print("1. Please Wear ID proof for verification.")
        print("2. Follow the Company security protocols and guidelines.")
        print("3. Maintain decorum and respect the workplace environment.")
        print("4. Smoking is strictly prohibited within the premises.")
        print("5. Return visitor badges and access cards before leaving the premises.")
        print("6. In case of any emergency, follow the instructions of the staff.")
        print("7. For any assistance, contact the reception or security personnel.")
        print("8. Report to the reception desk while exiting.\n")

def main():
    system = VisitorManagementSystem()
    while True:
        system.display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            system.check_in()
        elif choice == '2':
            system.check_out()
        elif choice == '3':
            system.visitor_guidance()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.") # pyright: ignore[reportUndefinedVariable]
            
main()