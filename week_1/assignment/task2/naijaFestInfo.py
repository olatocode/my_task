# Nigerian Festival Info
# Ask for:
    # Festival name (string)
    # Location (string)
    # Month held (string)
# Display the info with quotation marks around the festival name using escape sequences `(\")`.

festival_name = input("Enter the name of the festival: ")
location = input("Enter the location of the festival: ")
month = input("Enter the month the festival is held: ")
print(f"\"{festival_name}\" is held in {location} in {month}")