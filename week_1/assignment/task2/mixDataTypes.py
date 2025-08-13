# Mixing Data Types Ask the user for:
    # Your age (integer)
    # Your height in meters (float)
    # Your name (string)
# Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.

age = int(input("Enter your age (integer): "))
height = float(input("Enter your height in meters (float): "))
name = input("Enter your name (string): ")
print(f"My name is {name}, I am {age} years old and {height} meters tall.")
