
# ? Find the smallest and the second largest among three numbers.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

min_number = min(num1, num2, num3)
print(f"The smallest number among all three number is {min_number}")

max_number = max(num1, num2, num3)
print(f"The largest number among all three number is {max_number}")

middle_number = (num1 + num2 + num3) - max_number - min_number
print(f"The middle or second largest number is {middle_number}")
