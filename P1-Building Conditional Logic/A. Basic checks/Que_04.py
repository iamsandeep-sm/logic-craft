
# ? Find the largest of two numbers.
num1 = int(input("Enter you first number : "))
num2 = int(input("Enter you second number : "))
if num1 > num2:
    print(f"{num1} is the largest number among both the number you entered")
else:
    print(f"{num2} is the largest number among both the number you entered")
        
# * by using the max()
largest = max(num1 ,num2)
print(f"the largest number among both number is {largest}")

