
# ? Compute the number of days in a given month of a given year.

month = input("Enter Month (e.g., January, May, etc.): ").strip().title()
year = int(input("Enter Year (e.g., 2000, 2024): "))

month_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
month_30 = ['April', 'June', 'September', 'November']

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"{year} is a leap year.")
else:
    print("")

if month in month_31:
    print(f"{month} {year} has 31 days.")
elif month in month_30:
    print(f"{month} {year} has 30 days.")
elif month == 'February':
    if is_leap:
        print(f"February {year} has 29 days.")
    else:
        print(f"February {year} has 28 days.")
else:
    print("Error: Invalid month name entered. Please check your spelling.")

