tuple1= input("Enter any state in Nigeria").title()
tuple2= input("Enter any state in Nigeria").title()
tuple3= input("Enter any state in Nigeria").title()
tuple4= input("Enter any state in Nigeria").title()
tuple5= input("Enter any state in Nigeria").title()

statee = tuple1 , tuple2,  tuple3,  tuple4,  tuple5
turple_state = tuple(statee)

print(turple_state[0:4])
# check if lagos is in the turple and print "yes or no".
print("Lagos" in turple_state)
print(len(turple_state))


# # using if-else
# turple_state= input(tuple1, tuple2, tuple3, tuple4, tuple5)
# print(


if "Lagos" in statee: 
   print("Yes, lagos is present")
else: 
    print("No, Lagos is Absent")