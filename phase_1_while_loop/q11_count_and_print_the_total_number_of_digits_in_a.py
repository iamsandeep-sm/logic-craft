"""
Q11. Count and print the total number of digits in a given number.
"""
number = int(input("Enter any number : "))
original_number = number
count = 0
while number > 0:
    digit = number % 10
    count += 1
    number //= 10
print(f"your original number is {original_number}")
print(f"The number of digits you entered is {count}")
