
# ? Odd or even: determine whether a given number is odd or even.

number = int(input("Enter any number to check odd or even : "))
if number % 2 == 0:
    print(f"The entered number {number} is even")
else:
    print(f"The entered number {number} is odd")
