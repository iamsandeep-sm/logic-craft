
# ? Triangle validity: given three sides, check whether a triangle can be formed, then classify it as equilateral, isosceles or scalene.

# * • Equilateral: A triangle where all 3 sides are equal.
# * • Isosceles: A triangle where only 2 sides are equal.
# * • Scalene: A triangle where no sides are equal.

s1 = int(input("Enter length of side 1 : "))
s2 = int(input("Enter length of side 2 : "))
s3 = int(input("Enter length of side 3 : "))

if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2): # ! check valid triangle
    
    if s1 == s2 == s3:
        print("This is equilateral triangle")
    
    elif (s1 == s2) or (s1 == s3 ) or (s3 == s2 ):
        print("This is Isosceles triangle")
    else:
        print("This is Scalene triangle")
    
    