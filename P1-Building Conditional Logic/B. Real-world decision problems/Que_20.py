
# ? Simple calculator: read two numbers and an operator and print the result. Handle division by 0

a = int(input("Enter any number : "))
b = int(input("Enter any number : "))

print("\nWhich operation do you want to do:")
print(" for addition type [ add ]")
print(" for subtraction type [ sub ]")
print(" for multiplication type [ mul ]")
print(" for division type [ div ]\n")

operator = input("enter your operator : ")

if operator == 'add':
    add = a + b
    print(f"The result for operation is {add}")
    
elif operator == 'sub':
    sub = a - b
    print(f"The result for operation is {sub}")

elif operator == 'mul':
    mul = a * b
    print(f"The result for operation is {mul}")

elif operator == 'div':
    if b == 0:
        print("Error: divide by zero is not allowed")
    else:
        div = a / b
        print(f"The result for operation is {div}")
        
else:
    print("Invalid operator! Please try again and type add, sub, mul, or div.")


# ! ------------------------------------------------------------------------

# * using match method making this program more better ...........

operator = input("enter your operator : ")

match operator:
    case 'add':
        add = a + b
        print(f"The result for operation is {add}")
        
    case 'sub':
        sub = a - b
        print(f"The result for operation is {sub}")
        
    case 'mul':
        mul = a * b
        print(f"The result for operation is {mul}")
        
    case 'div':
        # Safely handle division by zero inside the case block
        if b == 0:
            print("Error: Division by zero is not allowed!")
        else:
            div = a / b
            print(f"The result for operation is {div}")
            
    case _:  # This is the default case if the user types an invalid operator
        print("Invalid operator! Please enter add, sub, mul, or div.")

