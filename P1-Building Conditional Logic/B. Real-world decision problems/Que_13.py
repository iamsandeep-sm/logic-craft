
# ? Income tax slab calculator for a given annual income (use any slab table).

# * tax = 0% for income between 0 to 300000
# * tax = 5% for income between 300000 to 500000
# * tax = 10% for income above 500000

actual_income = int(input("Enter your income : "))

if actual_income <= 300000:
    after_taxed = actual_income - (actual_income * 0 / 100) 
    print(f"your income after being taxed for is {after_taxed}")

elif actual_income <= 500000:
    below_5 = (actual_income - 300000) * 5 / 100
    after_taxed = actual_income - below_5
    print(f"your income after being taxed for is {after_taxed}")

else:
    above_5 = (actual_income - 500000 ) * 10 / 100
    check = (500000 - 300000 ) * 5 / 100
    # below_3 = actual_income * 0 / 100
    after_taxed = actual_income - (above_5 + check)
    print(f"your income after being taxed for is {after_taxed}")

# subtracting taxed amount from the actual_income of user.
# ! we can also code this program like this - 

total_tax = 0

if actual_income <= 300000:
    total_tax = 0

elif actual_income <= 500000:
    total_tax = (actual_income - 300000) * 5 / 100

else:
    above_5 = (actual_income - 500000) * 10 / 100
    check = (500000 - 300000) * 5 / 100
    total_tax = above_5 + check

after_taxed = actual_income - total_tax

print(f"Total Tax deducted: ₹{total_tax}")
print(f"Your income after tax is: ₹{after_taxed}")

