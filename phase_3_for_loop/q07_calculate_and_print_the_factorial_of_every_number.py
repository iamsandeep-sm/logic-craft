"""
Q7. Calculate and print the factorial of every number from 1 to n.
"""
n = int(input("Enter any number : "))
fact = 1
for i in range (1, n + 1):
    fact *= i
    print(f"factorial of {i} is {fact}")
