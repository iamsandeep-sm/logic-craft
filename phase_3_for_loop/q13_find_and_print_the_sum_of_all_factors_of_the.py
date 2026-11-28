"""
Q13. Find and print the sum of all factors of the given number.
"""
number = int(input("Enter any number : "))
sum_fact = 0
print(f"factors of your entered number {number} is down below-")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
        sum_fact += i
print(f"The sum of all factors is : {sum_fact}")
