# Nigerian Currency Converter (Very Advanced)
  # Ask for:
  # Amount in Naira (float)
  # Exchange rate to US Dollars (float)
# Exchange rate to British Pounds (float)
# Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.


naira = float(input("Enter amount in Naira (₦): "))
rate_usd = float(input("Enter exchange rate (₦ to $): "))
rate_gbp = float(input("Enter exchange rate (₦ to £): "))


usd = naira / rate_usd
gbp = naira / rate_gbp
print("\n================ CURRENCY CONVERTER ================\n")
print(f"{'Currency':<15}{'Amount':>20}")
print("----------------------------------------------------")
print(f"{'Naira (₦)':<15}{'₦' + format(naira, ',.2f'):>20}")
print(f"{'US Dollars ($)':<15}{'$' + format(usd, ',.2f'):>20}")
print(f"{'British Pounds (£)':<15}{'£' + format(gbp, ',.2f'):>20}")
print("====================================================\n")

