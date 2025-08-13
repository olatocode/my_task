# single quote
name = "Ada"
print(name)

# Double quote
greeting = "Hello"
print(greeting)

# Tripple quotes for (multi line strings)
story = '''Once upon a time,
ther was a coder name ada '''
print(story)

# string with numbers and symbols
password = "p@ssw0123"
print(password)


# String Operation
# Indexing
word = "Python"
print(word[0]) # p
print(word[-1]) # n



word = "python"
print(word[0-4])
print(word[2:])
print(word[:3])
print(word[::2])
print(word[::-1])

# string concatenation  $ repetition
# concatnation
a = "Hello"
b =  "World"
print(a + " " + b)

# Repition 
word = "Hi! "
print(word * 3)

# string searching and checking
# membership
text = "python programing"
print("python" in text)
print("Java" in text)


# find() / rfind()
text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7


# index() / rindex()
text = "Hello World"
print(text.index("World"))   # 6

# startswith() / endwith()

filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True


