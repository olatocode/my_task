# - Explain each output of the program below.
#- Give 3 usecases or cenarios where you can apply the program below.
#- Write the code for 1 of the 3 use cases.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")

# Checks if num1 is equal to num2.

# Returns True if they are equal, False otherwise.

print(f"{num1} != {num2} : {num1 != num2}")

# Checks if num1 is not equal to num2.

# Returns True if they are different, False if they are the same.

print(f"{num1} > {num2} : {num1 > num2}")

# Checks if num1 is greater than num2.

# Returns True if yes, False otherwise.

print(f"{num1} < {num2} : {num1 < num2}")

# Checks if num1 is less than num2.

# Returns True if yes, False otherwise.


# Use Cases / Scenarios

# 1 Age Verification in a Voting System

# Compare a user’s age with the legal voting age (e.g., 18).

# Example: if age >= 18: allow voting.

# 2  Price Comparison in Online Shopping

# Compare the price of two products to see which is cheaper or if they are equal.

# 3. Student Score Evaluation

# Compare two students’ test scores to see who scored higher, lower, or if they tied.


# Code for One Use Case (Age Verification in Voting System)
age = int(input("Enter your age: "))
voting_age = 18

print(f"Your age == Voting age : {age == voting_age}")
print(f"Your age != Voting age : {age != voting_age}")
print(f"Your age > Voting age : {age > voting_age}")
print(f"Your age < Voting age : {age < voting_age}")

if age >= voting_age:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


