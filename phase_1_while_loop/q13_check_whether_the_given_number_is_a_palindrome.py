"""
Q13. Check whether the given number is a palindrome.
"""
number = int(input("Enter any number : "))
org_number = number
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = (reversed_number * 10) +digit
    number //= 10
if org_number == reversed_number:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
