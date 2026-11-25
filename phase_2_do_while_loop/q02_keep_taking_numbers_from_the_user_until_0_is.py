"""
Q02. Keep taking numbers from the user until 0 is entered, then print the largest number among all inputs.
"""
print("The numbers will be added until you enter 0.")
temp = 0
n = int(input("Enter Number: "))
temp = n
while n != 0:
    n = int(input("Enter Number: "))
    if n > temp:
        temp = n

print("Largest number:", temp)
