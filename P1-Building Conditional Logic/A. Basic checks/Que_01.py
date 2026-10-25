
# ? Number identity: read a number and say whether it is positive, negative or zero.
number = int(input("Enter any number : "))
if number > 0:
    print(f"The number you entered {number} is positive")
elif number <0:
    print(f"The number you entered {number} is negative")
elif number == 0:
    print(f"The number you entered {number} is zero")
else:
    print("That's invalid input")
