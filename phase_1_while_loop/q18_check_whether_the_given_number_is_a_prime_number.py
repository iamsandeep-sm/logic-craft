"""
Q18. Check whether the given number is a prime number.
"""
number = int(input("Enter a number: "))
if number > 1:
    i = 2
    while i < number:
        if number % i == 0:
            print(number, "is not a prime number")
            break
        i += 1
    else:
        print(number, "is a prime number")
