
# ? Zodiac sign finder from day and month of birth.

#* this zodiac sign finder program takes the day and month of birth as input and determines the corresponding zodiac sign based on the provided date ranges. 
#! This is not work for the indian zodiac signs. it is based on the western astrology system.
zodiac = {
    "Capricorn": ((12, 22), (1, 19)),
    "Aquarius": ((1, 20), (2, 18)),
    "Pisces": ((2, 19), (3, 20)),
    "Aries": ((3, 21), (4, 19)),
    "Taurus": ((4, 20), (5, 20)),
    "Gemini": ((5, 21), (6, 20)),
    "Cancer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Scorpio": ((10, 23), (11, 21)),
    "Sagittarius": ((11, 22), (12, 21))
}   

day = int(input("Enter your birth day (1-31): "))
month = int(input("Enter your birth month (1-12): "))

if (month == 12 and day >= 22) or (month == 1 and day <= 19):
    sign = "Capricorn"
elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "Aquarius"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "Pisces"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    sign = "Gemini"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    sign = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "Libra"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "Scorpio"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "Sagittarius"
else:
    sign = "Unknown"


print("Your zodiac sign is : ", sign)
