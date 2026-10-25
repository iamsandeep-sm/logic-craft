
# ? Find the largest of three numbers without using max().

#* finding the largest number without using the max()
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1 > num2 and num1 > num3:
    print(f"The entered number {num1} is the largest number between all of them")
if num2 > num1 and num2 > num3:
    print(f"The entered number {num2} is the largest number between all of them")
else:
    print(f"The entered number {num3} is the largest number between all of them")
