"""
Q20. Find and print the sum of the Fibonacci series up to n terms.
"""
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
total = 0
if n <= 0:
    print("Please enter a positive integer.")
else:
    while count < n:
        total += a
        a, b = b, a + b
        count += 1
    print(f"The sum of the Fibonacci series up to {n} terms is {total}")
