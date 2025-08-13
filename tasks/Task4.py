# # Your Favorite Life Quote
quote = input("Enter your favorite quote: ")
title_case_quote = quote.title()
print(f"\"{title_case_quote}\"")

# Shopping List Manager
shopping_list = [input("Item 1: "), input("Item 2: "), input("Item 3: ")]
print(", ".join(shopping_list))

# Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")

# Name Organizer
names = input("Enter 5 names: ").split()
print(sorted([n.lower() for n in names]))

# Student Score Tracker
name = input("Enter name:"); 
score = input("score:"),
print("name","score")

# Word Analyzer
word = input("Enter a word:")
print(len(word), word[::-1])

# List Manipulation
city = ["Ikeja", "Ibadan", "Abeokuta", "Akure", "Ilorin" ]; 
city[1] = input("Enter a new city: ")
city.pop()
city.insert(0,input ("New city at start: ")) 
print(city)