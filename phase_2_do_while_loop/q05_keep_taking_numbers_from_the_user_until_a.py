"""
Q05. Keep taking numbers from the user until a negative number is entered, then count how many positive numbers were entered.
"""
number = int(input("Enter any number: "))
count = 0
while number >= 0:
    if number > 0:
        count += 1
    number = int(input("Enter another number: "))
print(f"Positive number you entered is {count}")
