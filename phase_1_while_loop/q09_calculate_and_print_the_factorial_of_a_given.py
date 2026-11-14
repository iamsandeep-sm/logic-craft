"""
Q9. Calculate and print the factorial of a given number.
"""
n = int(input("Enter any number: "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)

