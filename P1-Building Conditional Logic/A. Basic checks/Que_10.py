# ? Print the day name for a number between 1 and 7 (use if-else, then switch or match)
# ! first we use if-else.

day = int(input("Enter the day : "))
if day == 1:
    print("The day is Monday")
elif day == 2:
    print("The day is Tuesday")
elif day == 3:
    print("The day is Wednesday")
elif day == 4:
    print("The day is Thursday")
elif day == 5:
    print("The day is Friday")
elif day == 6:
    print("The day is Saturday")
elif day == 7:
    print("The day is sunday")
else:
    print("The day is invalid that you enter")

# ! now using the match in python ------

match day:
    case 1:
        print("The day Monday")
    case 2:
        print("The day is Tuesday")
    case 3:
        print("The day is Wednesday")
    case 4:
        print("The day is Thursday")
    case 5:
        print("The day is Friday")
    case 6:
        print("The day is Saturday")
    case 7:
        print("The day is Sunday")
    case _:    
        print("you have entered invalid number")

