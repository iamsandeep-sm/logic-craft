"""
Q3. Print all even numbers between 1 and 100.
"""
i = 2
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
    # i += 2  ##* if don't want to use the if condition, then we can use this line instead of the above line and make sure to start i from 2. and don't need to write the if condition in that case.
    