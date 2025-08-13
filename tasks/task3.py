# task 1
#Write a program to take a string input from the user and display it in uppercase.
userString = input("Enter a string input: ")
print(userString.upper())

text = "python"
print(text[:1])
print(text[5:])


name = input("Enter your name: ")
print(f"Hello, (name)!")



text = "AI Engineer"
print(sum(1 for _ in  text))

text = "Hello, World"
print(text.replace("Hello, World", "python"))


# Task 2
# Check if a given string contains the substring "python" (case-insensitive).
text = "Hello, World"
print("python" in text.lower())

# Write a program to reverse a string without using slicing ([::-1]).
text = "Hello, World"
print(text[::-1])   

# Given a string with extra spaces, remove the leading and trailing spaces.
text = "   Hello, World   "
print(text.strip())

# Ask the user to enter a sentence and print the number of vowels in it.
text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
print(sum(1 for char in text if char in vowels))   

# Convert a string "1234" to an integer and multiply it by 2.
text = "1234"
print(int(text) * 2)    

# Task 3
# Given "apple,banana,orange", split the string into a list of fruits.
text = "apple,banana,orange"
print(text.split(","))  

# Ask the user for a sentence and print each word on a new line.
text = input("Enter a sentence: ")
for word in text.split():
    print(word) 

# Replace all spaces in a string with underscores (_).
text = "Hello, World"
print(text.replace(" ", "_"))   

# Count how many times the letter "a" appears in "Banana".
text = "Banana"
print(text.count("a"))  

# Check if a given string starts with "https://".
text = "https://example.com"
print(text.startswith("https://"))