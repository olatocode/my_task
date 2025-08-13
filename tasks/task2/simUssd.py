# Simulated USSD Menu Interaction
 # You are to design a mock USSD interface for a mobile service.
 # Requirements:
   # When the user runs the program, display a welcome screen with a Nigerian context greeting.
   # Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
   # Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
   # Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
   # Use f-strings and/or concatenation to display a confirmation message showing the selected option.
   # Ask for an amount (if applicable) and store it as a number using type casting.
   # Display a final message summarizing the transaction.

# Welcome screen
print("Welcome to Naija Mobile Service!")
print("How far? Hope your day dey go well.\n")

# Dial USSD code
ussd_code = input("Please dial a USSD code (e.g., *123#): ")

# Menu
print("\n--- MAIN MENU ---")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# Choice
choice = input("\nEnter your choice (1, 2, or 3): ")

# Store options in variables
option1 = "Check Balance"
option2 = "Buy Airtime"
option3 = "Buy Data"

# Display chosen option
print("\nYou selected: " + option1 * (choice == "1") + option2 * (choice == "2") + option3 * (choice == "3"))

# Amount input (only meaningful if choice is 2 or 3)
amount = input("Enter amount in Naira: ")

# Summary
print(f"\nTransaction Summary:\nOption: {option1 * (choice == '1') + option2 * (choice == '2') + option3 * (choice == '3')}\nAmount: ₦{amount}")
