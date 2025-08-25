# Task 5
# Contact Quick Lookup
names = ("Tobi", "Taiwo", "Bukayo")
phone_num = (+23470692345, +234809185789, +23480904400)
contact_dict = {name: phone for name, phone in zip(names, phone_num)}
lookup_name = input ("kindly enter the missing name: ")
if lookup_name in names:
    print(f"the corresponding phone number for {lookup_name} is {contact_dict}")
else:
    print("contact not found")
    # print (contact_dict)
