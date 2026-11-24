"""
Q16. Check whether the given number is a Perfect number.
"""
'''
what is perfect number? lets understand in short with example.
A perfect number is a positive integer that is equal to the sum of its proper divisors
eg. 6 is a perfect number
because its proper divisors are 1, 2, and 3, and their sum is 1 + 2 + 3 = 6.
* 28 is also a perfect number,
28 divided by 1, 2, 4, 7, and 14
sum -> 1 + 2 + 4 + 7 + 14 = 28.
'''
num = int(input("Enter a number: "))
i = 1
divisor_sum = 0
while i < num:
    if num % i == 0:
        divisor_sum += i
    i += 1

if divisor_sum == num and num > 0:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

