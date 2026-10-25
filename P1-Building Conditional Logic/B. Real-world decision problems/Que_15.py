
# ? Given three angles, check whether they form a valid triangle.

a1 = int(input("Enter angle for triangle : "))
a2 = int(input("Enter angle for triangle : "))
a3 = int(input("Enter angle for triangle : "))

if a1 > 0 and a2 > 0 and a3 > 0:

    if (a1 + a2 + a3) == 180:
        print("This is valid triangle")
    else:
        print("This is not valid triangle")
else:
    print("Angels must be greater than 0")

