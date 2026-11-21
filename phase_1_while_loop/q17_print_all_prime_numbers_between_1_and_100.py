"""
Q17. Print all prime numbers between 1 and 100.
"""
i = 2
while i <= 100:
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        print(i)
    i += 1

