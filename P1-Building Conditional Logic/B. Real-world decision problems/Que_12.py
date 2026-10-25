
# ? Electricity bill: first 100 units at one rate, next 100 at another, rest at a higher rate. Print the bill.

# * unit from 1 to 100 ----> 4/-
# * unit from 101 to 200 ----> 5/-
# * unit from 201 + ----> 7/- Fixed

unit_ask = float(input("Enter you unit for electricity Bill : "))

if unit_ask <= 100:
    Bill = unit_ask * 4
    print(f"Your Electricity bill for {unit_ask} is {Bill}/-")

elif unit_ask <= 200:
    below_200 = unit_ask - 100
    under_100 = unit_ask - below_200
    Bill = (under_100 * 4) + (below_200 * 5)
    print(f"Your Electricity Bill for {unit_ask} is {Bill}/-")
    
else:
    for_first_100 = 100 * 4
    for_above_100 = 100 * 5
    current_ask = (unit_ask - 200) * 7
    Bill = current_ask + for_first_100 + for_above_100
    print(f"Your Electricity Bill for {unit_ask} is {Bill}/-")  
    
# ! note for myself - In Python, if an if statement checks unit_ask <= 100, the next elif already knows that unit_ask must be greater than 100.

# * i can also do this code like this -

unit_ask = float(input("Enter your unit for electricity Bill: "))

# Condition 1 to 100 units
if unit_ask <= 100:
    Bill = unit_ask * 4

# Condition 101 to 200 units
elif unit_ask <= 200:
    # First 100 units at 4/-, remaining units at 5/-
    Bill = (100 * 4) + ((unit_ask - 100) * 5)

# Condition 201 units and above
else:
    # First 100 at 4/-, next 100 at 5/-, and the rest at 7/-
    Bill = (100 * 4) + (100 * 5) + ((unit_ask - 200) * 7)

print(f"Your Electricity bill for {unit_ask} units is {Bill}/-")

