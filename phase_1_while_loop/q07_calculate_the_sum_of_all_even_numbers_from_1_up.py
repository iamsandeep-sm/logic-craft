"""
Q7. Calculate the sum of all even numbers from 1 up to n.
"""
n = int(input("Enter any number: "))
i = 2
total = 0
while i <= n:
    total += i
    i += 2
print(total)
        