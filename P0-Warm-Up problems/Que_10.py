import math
# ? Read a float and print it rounded to 2 decimal places and as an integer (floor and ceil).

number = float(input("Enter any number using the decimal : "))
print(f"The entered number with 2 decimal place is : {number:.2f}")

# * we can write this program as using the inbuilt method round()
# * print(round(number, 2))   -----> output will be same for both the program.

import math  # Required for floor and ceil functions

# 2. Floor (rounds down to nearest integer)
print(f"Floor integer: {math.floor(number)}")

# 3. Ceil (rounds up to nearest integer)
print(f"Ceil integer: {math.ceil(number)}")
