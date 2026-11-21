"""
Q21. Print the square of each number from 1 to n.
"""
n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a positive number greater than 0.")
else:
    i = 1
    print("Square of each number till the number you entered - ")
    while i <= n:
        print(f"{i} X {i} = {i*i}")
        i += 1
