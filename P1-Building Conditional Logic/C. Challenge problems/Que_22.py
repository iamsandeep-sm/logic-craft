
# ? Given the three sides, check whether the triangle is right-angled.

s1 = 50
s2 = 80
s3 = 50

# 1. Check if the sides can actually form a valid triangle
# Rule: The sum of any two sides must be GREATER than the third side
if s1 > 0 and s2 > 0 and s3 > 0:
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        print("The triangle is valid")
        
        # 2. Check if it's a right-angled triangle using Pythagoras (a² + b² = c²)
        # We check all three possibilities since we don't know which one is the longest
        if (s1**2 + s2**2 == s3**2) or (s1**2 + s3**2 == s2**2) or (s2**2 + s3**2 == s1**2):
            print("This is a right-angled triangle")
        else:
            print("This is not a right-angled triangle")
            
    else:
        print("The triangle is not valid (sides don't connect)")
else:
    print("Please enter numbers greater than 0")

# ! -----------------------------  -------------------------------  -----------------------------

# * this is another method to this same problem......

def is_right_angled_triangle(a, b, c):
    # Step 1: Put sides in a list and sort them
    sides = sorted([a, b, c])
    
    # After sorting:
    # sides[0] is the shortest side
    # sides[1] is the middle side
    # sides[2] is the longest side (hypotenuse)
    
    # Step 2: Check the Pythagorean condition (a^2 + b^2 == c^2)
    if (sides[0]**2 + sides[1]**2) == sides[2]**2:
        return True
    else:
        return False

# --- Testing the logic ---
# Example 1: Should be True (3^2 + 4^2 = 5^2 -> 9 + 16 = 25)
print(is_right_angled_triangle(3, 4, 5))  # Output: True

# Example 2: Should be False (5^2 + 6^2 != 8^2 -> 25 + 36 != 64)
print(is_right_angled_triangle(5, 6, 8))  # Output: False


