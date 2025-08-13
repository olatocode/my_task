# using parenthese
# Example 1: tuple with multiple items
fruits = ("Apple", "banana", "cherry")
food = 'Rice'
print(fruits, food) 

# Without parentheses (tuple packing)
numbers = 1,2,3
print(numbers)


# Single-item tuple (must include a comma)
single_item = ("Apple",)
print(single_item)
print(type(single_item))

# Using the tuple() constructor
fruits_list = ["Apple", "Banana", "Cherry"]
fruit_tuple = tuple(fruits_list)
print(fruits_list)

# ordered
colors = ("red", "green", "blue")
print(colors[0])

# Immutable (shows an error)
# colors[1] = "yellow"
# print(colors)

# Alloow duplicate
numbers = 1,2,2,3
print(numbers)

# mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# Nested turples 
nested = (("a", "b"), (1,2))
print(nested) 

# indexing
fruits = ("Apple", "Banana", "cherry")
print(fruits[0])
print(fruits[-1])

