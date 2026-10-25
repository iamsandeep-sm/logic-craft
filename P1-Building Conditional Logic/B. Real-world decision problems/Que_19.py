
# ? ATM logic: given balance, withdrawal amount and a multiple-of-100 rule, decide whether the withdrawal is allowed.

balance = 15652
with_amount = int(input("Enter your amount to withdrawal : "))

if with_amount <= balance:
    if with_amount % 100 != 0: # multiple of 100 rule
        print("User this Amount cannot be withdrawn please enter like: 100/200/500/1000....")
    else:
        print("This Amount can be withdrawn")
else:
    print("User you didn't have enough balance")
    
# !     Another Code    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 

balance = 15652
with_amount = int(input("Enter your amount to withdraw: "))

if with_amount > balance:
    print("Error: You do not have enough balance.")

elif with_amount % 100 != 0:
    print("Error: This amount cannot be withdrawn. Please enter a multiple of 100 (e.g., 100, 200, 500, 1000).")

else:
    remaining_balance = balance - with_amount
    print(f"Success! This amount can be withdrawn.")
    print(f"Your remaining balance is: {remaining_balance}")
    
