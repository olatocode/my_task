# School Fees Breakdown
  # Ask for:
    # School name
    # Tuition fee (float)
    # Hostel fee (float)
    # Feeding fee (float)

# Calculate the total and print it in receipt format with each fee on a new line.

school_name = input("Enter the name of the school: ")
tuition_fee = float(input("Enter the tuition fee: "))
hostel_fee = float(input("Enter the hostel fee: "))
feeding_fee = float(input("Enter the feeding fee: "))

total = tuition_fee + hostel_fee + feeding_fee

print("School Name: " + school_name)
print("Tuition Fee: " + str(tuition_fee))
print("Hostel Fee: " + str(hostel_fee))
print("Feeding Fee: " + str(feeding_fee))
print("Total: " + str(total))