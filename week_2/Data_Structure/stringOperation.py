# # convert all characters in the string to Uppercase
# name = "Ada Balogun"
# print(name.upper())
# print(name.title())

# # convert all characters in the string to Lowercase
# sentence = "Python is amazing"
# print(sentence.lower())


# # remove whitespace
# text = " Abuja "
# print(text.strip())

# # replace occurrence of substring with another another substring
# message = "I love Java"
# print(message.replace("java", "Python"))  

# # switches lowercase to uppercase and vice-versa
# text = "Hello ABEOKUTA"
# print(text.swapcase())  


# # remove whitespace or specific characters from the left side only
# text = "   Nigeria"
# print(text.lstrip())  

# # remove whitespace or specific characters from the right side only
# text = "Nigeria   "
# print(text.rstrip())  

# # split a string into a list using a seperator (default is a space)
# fruits = "mango orange banana"
# print(fruits.split())  

# # split a string into a list from the right side
# text = "one,two,three,four"
# print(text.rsplit(",", 2))  

# # split a string into a list at each new line
# lines = "Line 1\nLine 2\nLine 3"
# print(lines.splitlines())  


# # Joins a list of strings into one string with a specified separator.
# words = ["I", "love", "Python"]
# print(" ".join(words))  

# center the string within a specified width, padding with space or characters
text = "Python"
print(text.center(20, "-"))  


# Left-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.ljust(10, "*"))  

# right-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.rjust(10, "*"))  

# Pads a numeric string on the left with zeros until it reaches a given length.
num = "42"
print(num.zfill(5))

# check if the string contains only letters
print("lagos".isalpha())
print("lagos".isdigit())


# check if the string contains only letters and digits
print("python3".isalnum())
print("python 3".isalnum())

# Revers string
text = "world"
print(text[::-1])

