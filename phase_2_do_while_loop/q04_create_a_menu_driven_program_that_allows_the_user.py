"""
Q04. Create a menu-driven program that allows the user to choose and perform different operations.
"""
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the another number: "))
print("Operation for addition - add \n for subtraction - sub \n for multiplication - mul \n for divide - div")
operation =  input("Enter operation : ")
while operation == "add" or operation == "sub" or operation == "mul" or operation == "div":
    if operation == "add":
        print(n1 + n2)
    elif operation == "sub":
        print(n1 - n2)
    elif operation == "mul":
        print(n1 * n2)
    elif operation == "div":
        print(n1 / n2)
    operation = input("Please Enter exact operation")
    