"""
Q6. Calculate and print the factorial of a given number.
"""
number = int(input("Enter any number for the factorial of that number : "))
fact = 1
for i in range (1, number + 1):
    fact *= i
print(f"The factorial of {number} is : {fact}")
