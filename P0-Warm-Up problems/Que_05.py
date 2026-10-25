import math  # because using the pi for calculation in this problem importing the math package
#? Read the radius and print the area and circumference of a circle.

r = int(input("Enter the radius of circle : "))
# area of circle is pi*(r**2) and circumference of circle is 2 * pi *r
area = math.pi *(r**2)
circ = 2 * math.pi *r
print(f"area of circle is : {area:.2f}")
print(f"circumference of circle is : {circ:.2f}")
