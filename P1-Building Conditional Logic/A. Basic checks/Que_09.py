
# ? Check whether a given age qualifies for voting, driving and senior discount.

age = int(input("Enter your age :"))
if age <=17:
    print(f"You are {age} year old, you are not eligible for voting and driving license ")
if age >= 18:
    print(f"You are {age} year old, you are eligible for voting and driving license ")
if age >= 60:
    print("You will receive the senior discount for begin senior")
