# Transport Fare Calculator
 # Ask for:
    # Distance in km (float)
    # Fare per km (float)
# Calculate and display the total fare with two decimal places using `f"{value:.2f}"`.

distance = float(input("Enter the distance in km: "))
fare_per_km = float(input("Enter the fare per km: "))
total_fare = distance * fare_per_km
print(f"The total fare is: {total_fare:.2f}")
