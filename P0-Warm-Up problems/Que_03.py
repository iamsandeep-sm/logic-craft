## Warm-Up problems
# ? Swap two variables, first using a third variable, then without one.

n1 = 5
n2 = 10
#* with using the third variable first -----
print(f"Without swapping the values n1 : {n1} and n2 : {n2}")
new = n1
n1 = n2
n2 =new
print(f"After swapping the values n1 : {n1} and n2 : {n2}")


#* without using the third variable ------
num1 = 50
num2 = 100
print(f"before swapping the values num1 : {num1} and num2 : {num2}")
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"after swapping the values num1 : {num1} and num2 : {num2}")

#* the another method used in python for swapping number without the third variable
mark1 = 37
mark2 = 85
mark1, mark2 = mark2, mark1    #! important working in python
print(f"mark1 : {mark1} and mark2 : {mark2}")