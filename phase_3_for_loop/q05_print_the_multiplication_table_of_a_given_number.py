"""
Q5. Print the multiplication table of a given number.
"""
number = int(input("Enter any number for the multiplication of that number : "))
for i in range(1, 11):
    print(f"{number} X {i} = {number*i}")
