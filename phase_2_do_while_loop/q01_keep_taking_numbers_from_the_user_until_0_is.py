"""
Q01. Keep taking numbers from the user until 0 is entered, then print the sum of all entered numbers.
"""
print("The numbers will be added until you enter 0.")

total = 0
n = int(input("Enter any Number: "))
total += n

while n != 0:
    n = int(input("Enter any Number: "))
    total += n

print("Sum of all entered numbers:", total)
