"""
Q10. Find and print the product of all digits of a given number.
"""
number = int(input("Enter any number : "))
product = 1
count = 0
while number > 0:
    digit = number % 10 # this print the unit / last digit of the number entered by the user
    count += 1 # this will count the number of digits
    product *= digit # this will multiply the digits of that entered number
    number //= 10 # this will remove the last digit of that entered number so that move to next digit
print(f"The product of all digits is : {product}")
print(f"Number of digits is : {count}")
