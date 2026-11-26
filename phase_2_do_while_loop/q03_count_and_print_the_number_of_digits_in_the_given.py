"""
Q03. Count and print the number of digits in the given number.
"""
number = int(input("Enter a number: "))
count = 0
if number == 0:
    count = 1
while number != 0:
    number //= 10
    count += 1
print("Number of digits:", count)
