# Stimulate USSD Menu Interaction
intro = print("Welcome to MTN customer service we are everywhere you go")
code = (" dial *123# to check all our services" )
checked_balance =input (" check your balance")
Buy_Airtime = input(" buy your airtime")
Buy_Data = input (" buy your data service ") 
print(f"  check your balance {"checked_balance"}.\n buy your airtime {"Buy Airtime"}.\n and lastly to buy data press{"Buy_Data"} ")
Choose_offer = (" choose an offer between {1,2,3} {Buy_Data}")


# if else statement
checked_balance= 5000
Buy_Airtime= 1000

if checked_balance >= Buy_Airtime:
    print("PURCHASE SUCCESSFUL") 
else:
    print("INSUFFICIENT BALANCE")


    # Using try method
try:
    checked_balance = float(Buy_Airtime) 
    if checked_balance > Buy_Airtime:
        raise ValueError("Insufficient funds.")
    
    Buy_Airtime -= checked_balance
    print("Withdraw successful.  New balance: is", checked_balance)
except ValueError as e:
    print("Error", e)

except Exception as e:
    print("unexpected error:", e)

finally:
    print("Transaction session closed.")