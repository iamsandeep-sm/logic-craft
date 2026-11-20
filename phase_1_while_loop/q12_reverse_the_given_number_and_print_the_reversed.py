"""
Q12. Reverse the given number and print the reversed value.
"""
number = 1234567
org_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) +digit
    number //= 10
print(f"The reversed number for {org_number} is {reversed_number}")
