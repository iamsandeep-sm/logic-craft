"""
Q23. Print all numbers between a and b that are divisible by 7.
"""
print("You have to enter the two points a and b between which, finding the numbers divisible by 7")
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
current = a
while current <= b:
    if current % 7 == 0:
        print(current)
    current += 1
    