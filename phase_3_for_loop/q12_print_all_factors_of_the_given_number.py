"""
Q12. Print all factors of the given number.
"""
number = int(input("Enter any number : "))
print(f"factors of your entered {number} is - ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
