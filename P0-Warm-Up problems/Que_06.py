
#? Read a 3-digit number and print the sum of its digits (use / and % only).

number = int(input("Enter any 3-Digit number : "))
unit = number % 10
ten = (number // 10) % 10
hundred = number // 100
sum_number = unit + ten + hundred
print(sum_number)

