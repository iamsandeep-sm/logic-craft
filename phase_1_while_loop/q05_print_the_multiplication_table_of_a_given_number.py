"""
Q5. Print the multiplication table of a given number from n × 1 to n × 10.
"""
n = int(input("Enter any number: "))
i = 1
while i <= 10:
    t = n * i 
    print(f"{n} X {i} = {t}")
    i += 1