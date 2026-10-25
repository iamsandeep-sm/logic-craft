
# ? Leap year, valid date: given day, month and year, check whether the date is valid.

date = int(input("Enter date : "))
month = int(input("Enter month : "))
year = int(input("Enter year : "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if date < 1 or date > 31 and month < 1 or month > 12:
    print("Sorry This is invalid input please enter valid Date and Month")
elif month == 2:
    if is_leap and date <= 29:
        print("This is valid and year is Leap year")
    elif not is_leap and date <= 28:
        print("This is valid date and year is normal not a leap year")
    else:
        print("This is not valid, February month does'nt have this many days")

elif month in [4, 6, 9, 11] and date > 30:
    print("Invalid")
else:
    print("The date is valid")
