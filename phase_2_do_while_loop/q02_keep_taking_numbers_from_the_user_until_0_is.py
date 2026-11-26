"""
Q02. Keep taking numbers from the user until 0 is entered, then print the largest number among all inputs.
"""
print("The numbers will be added until you enter 0.")
largest = 0
n = int(input("Enter Number: "))
while n != 0:
    n = int(input("Enter Number: "))
    if n > largest:
        largest = n

print("Largest number:", largest)
