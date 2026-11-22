"""
Q25. Find and print the sum of all factors of the given number.
"""
number = int(input("Enter the number to find its factors: "))
print("The factors of given number are -")
i = 1
fact_sum = 0
while i <= number:
    if number % i == 0:
        print(i)
        fact_sum += i
    i += 1
print(f"The sum of the factors of entered number is : {fact_sum}")
