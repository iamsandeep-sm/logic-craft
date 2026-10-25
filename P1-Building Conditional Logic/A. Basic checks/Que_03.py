
# ? Divisibility check: check whether a number is divisible by 3, by 5, and by both.

number = int(input("Enter any number to check its divisibility by 3, 5, both : "))
if number % 3 == 0 and number % 5 == 0:
    print("The number is divisible by both 3 and 5")
elif number % 3 == 0:
    print("The number is divisible by 3")
elif number % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is neither divisible by 3 nor 5")     
    
    