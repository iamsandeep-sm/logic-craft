"""
Q24. Print all factors of the given number.
"""
number = int(input("Enter the number to find its factors: "))
print("The factors of given number are -")
i = 1
while i <= number:
    if number % i == 0:
        print(i)
    i += 1
