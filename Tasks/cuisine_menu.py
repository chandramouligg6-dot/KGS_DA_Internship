#WAL to Menue with 3 cuisine with 6 dishes in each using if,elif, else statements 

# Welcome message
print("-----------WELCOME TO THE GRAND KGS CAFETERIA----------")

print("Please select a cuisine: ")
print("1. Italian")
print("2. Indian")
print("3. Chinese")

# Get cuisine choice
cuisine_choice = input("Enter cuisine number (1-3): ")

# if: Check if cuisine choice is valid
if cuisine_choice == "1":
    print("\n--- ITALIAN MENU ---")
    print("1. Margherita Pizza - $12")
    print("2. Pasta Carbonara - $14")
    print("3. Mushroom Risotto - $15")
    print("4. Vegetable Lasagna - $13")
    
    # Inner if: Get dish choice for Italian
    dish_choice = input("\n Select a dish (1-4): ")
    
    if dish_choice == "1":
        print("\n You ordered: Margherita Pizza ($12). \n Enjoy your meal! \n")
    elif dish_choice == "2":
        print("\n You ordered: Pasta Carbonara ($14). \n Enjoy your meal! \n")
    elif dish_choice == "3":
        print("\n You ordered: Mushroom Risotto ($15). \n Enjoy your meal! \n")
    elif dish_choice == "4":
        print("\n You ordered: Vegetable Lasagna ($13). \n Enjoy your meal! \n")
    else:
        print("\n Invalid dish choice! Please select a number between 1 and 6.")

elif cuisine_choice == "2":
    print("\n--- INDIAN MENU ---")
    print("1. Butter Chicken - $15")
    print("2. Paneer Butter Masala - $13")
    print("3. Dal Makhani - $11")
    print("4. Chicken Biryani - $14")
    
    # Inner if: Get dish choice for Indian
    dish_choice = input("\n Select a dish (1-4): ")
    
    if dish_choice == "1":
        print("\n You ordered: Butter Chicken ($15). \n Enjoy your meal! \n")
    elif dish_choice == "2":
        print("\n You ordered: Paneer Butter Masala ($13). \n Enjoy your meal! \n")
    elif dish_choice == "3":
        print("\n You ordered: Dal Makhani ($11). \n Enjoy your meal! \n ")
    elif dish_choice == "4":
        print("\n You ordered: Chicken Biryani ($14). Enjoy your meal! \n")
    else:
        print("\n Invalid dish choice! Please select a number between 1 and 6.")

elif cuisine_choice == "3":
    print("\n--- CHINESE MENU ---")
    print("1. Vegetable Fried Rice - $10")
    print("2. Hakka Noodles - $11")
    print("3. Vegetable Spring Rolls - $8")
    print("4. Chicken Manchurian - $13")
    
    # Inner if: Get dish choice for Chinese
    dish_choice = input("\n Select a dish (1-4): ")
    
    if dish_choice == "1":
        print("\n You ordered: Vegetable Fried Rice ($10). \n Enjoy your meal! \n")
    elif dish_choice == "2":
        print("\n You ordered: Hakka Noodles ($11). \n Enjoy your meal! \n")
    elif dish_choice == "3":
        print("\n You ordered: Vegetable Spring Rolls ($8). \n Enjoy your meal! \n")
    elif dish_choice == "4":
        print("\n You ordered: Chicken Manchurian ($13). \n Enjoy your meal! \n")
    else:
        print("\n Invalid dish choice! Please select a number between 1 and 6.")

else:
    print("\n Invalid cuisine choice! Please select 1, 2, or 3.")