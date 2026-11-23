"""
Q16. Check whether the given number is a Perfect number.
"""
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
''''''
