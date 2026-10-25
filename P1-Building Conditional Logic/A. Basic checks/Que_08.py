
# ? Check whether a year is a leap year (divisible by 4, but century years only if divisible by 400).

year = int(input("Enter any year to check leap year : "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"The {year} is leap year")
else:
    print(f"The {year} is not a leap year")

# ! -----------------------------------------------------------

# * for better error handling if any user enter the invalid number or anything
# ! we use Try and Except block
try:
    year = int(input("Enter any year to check leap year : "))
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"The {year} is a leap year.")
    else:
        print(f"The {year} is not a leap year.")
except ValueError:
    print("Please enter a valid structure of numbers (e.g., 2024).")

