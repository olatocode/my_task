# create and display
# naija_dish = (

#     input("Enter first dish: "),
#     input("Enter second dish: "),
#     input("Enter third dish: ")
# )
# print(naija_dish)
# print("\n".join(naija_dish))


# tuple and input
# friends = (
#     input("Enter first name: "),
#     input("Enter second name: "),
#     input("Enter third name: "),
#     input("Enter fourth name: "),
#     input("Enter fifth name: ")
# )

# print(friends[::-1])

# turple operation
# states = (
#      input("Enter first state: "),
#     input("Enter second state: "),
#     input("Enter third state: "),
#     input("Enter fourth state: "),
#     input("Enter fifth state: ")
# )

# print("print lagos there: ", "Yes" if "lagos" in states else "No")
# print("first state", [0])
# print("last state", [-1])


#turple Unpacking
# profile = (
#     input("Enter firstname: "),
#     float(input("Enter age: ")),
#     input("Enter favourite color: "),
#     input("Enter home town: ")
# )

# firstname, age, favorite_color, home_town = profile
# print(firstname, "\n")
# print(age, "\n")
# print(favorite_color, "\n")
# print(home_town, "\n")

# modify turple indirectly
shopping_list = (
    input("Enter first item: "),
    input("Enter second item: "),
    input("Enter third item: "),
)

shopping_list = list(shopping_list)
shopping_list.append(input("Enter fourth item : "))
shopping_list.append(input("Enter fifth item : "))
shopping_list = tuple(shopping_list)
print("updated shopping list")
print(" | ".join(shopping_list))


# Attendace tracker
days_of_week  = ("Monday", "Tuesday", "Wenesday", "Thursday", "Friday")
month_of_year = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

student = input("Enter your name: ")
gender = input("Enter your gender: ")
course_track = input("Enter your course: ")

current_month_num = float(input("Enter your current month number(1-1): "))
current_day_num = float(input("Enter your current day number(1-7): "))

