# Online Store Cart Calculation
# create a list of items "Book", "pen", "Bag" and another list of prices 500, 100, 2000
items=  ["Book", "pen", "Bag"]
price =[500, 100, 2000]

cart_total = 0

cart_total+= price[0]
cart_total+=price[1]
cart_total+=price[2]
print(cart_total)

print(f"the list of items:{items} and total price:{cart_total}")

if "Car" in items: 
   print("this are the price items for your shopping")
else:
    print("this is not included in your shopping list")