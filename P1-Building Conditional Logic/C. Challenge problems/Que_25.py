
# ? Compare two dates and print which one comes earlier.

from datetime import datetime

# 1. Define date strings (Day-Month-Year)
date_a = "15-05-2026"
date_b = "23-10-2026"

# 2. Convert text strings using the matching blueprint
calendar_date_a = datetime.strptime(date_a, "%d-%m-%Y")
calendar_date_b = datetime.strptime(date_b, "%d-%m-%Y")

# 3. Compare them
if calendar_date_a < calendar_date_b:
    print(f"{date_a} comes earlier!")
elif calendar_date_a > calendar_date_b:
    print(f"{date_b} comes earlier!")
else:
    print("Both dates are the same!")
