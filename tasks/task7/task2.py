# Super Market Price List
item_list= ["bag", "plate", "shoe"]
price_item_1 = int(input("kindly input the price of item one:"))
price_item_2 = int(input("kindly input the price of item two:"))
price_item_3 = int(input("kindly input the price for item three: "))

dict_of_items = {}
dict_of_items[item_list[0]] = price_item_1
dict_of_items[item_list[1]] = price_item_2
dict_of_items[item_list[2]] =price_item_3
print(dict_of_items)
name_update = input("kindly input the name of the items you want to add:")
price_update = input("enter the updated price of the item you imputed: ")
print(name_update in dict_of_items.keys())