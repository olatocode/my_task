# Daily market Report Ask the user to input:
  # Market name
 # Number of traders
 # Daily revenue in naira
 # Display the result using f-string formatting with commas for thousands separator.

market_name = input("Enter the name of the market: ")
traders = int(input("Enter the number of traders: "))
revenue = float(input("Enter the daily revenue in naira: "))
print(f"Market name: {market_name}")
print(f"Number of traders: {traders}")
print(f"Daily revenue in naira: {revenue}")