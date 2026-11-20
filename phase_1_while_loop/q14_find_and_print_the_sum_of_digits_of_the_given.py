"""
Q14. Find and print the sum of digits of the given number.
"""
number = int(input("Enter any number : "))
org_num = number
sum = 0
while number > 0:
    digit = number % 10
    sum += digit
    number //= 10
print(f" the number you entered is {org_num} and the sum of digit of this number is {sum}")
