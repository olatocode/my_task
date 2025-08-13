# Electricity Bill Formatter  - Ask for:
     #Customer’s full name
   # Units consumed (kWh) – integer
   # Cost per unit – float
# Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.


name = input(" Enter Customer's full name: ").strip()
units = int(input(" Enter Units consumed (kWh): ").strip())
cost_per_unit = float(input(" Enter Cost per unit: ").strip())

# Calculate total
total = units * cost_per_unit

# Create receipt
receipt = (
    "================ ELECTRICITY BILL ================\n"
    f"Customer: {name}\n"
    "--------------------------------------------------\n"
    f"Units Consumed:\t{units} kWh\n"
    f"Cost / Unit:\t{cost_per_unit:.2f}\n"
    "--------------------------------------------------\n"
    f"TOTAL DUE:\t{total:.2f}\n"
    "==================================================\n"
    "Thank you for your prompt payment.\n"
)

# Print the receipt
print("\n" + receipt)
