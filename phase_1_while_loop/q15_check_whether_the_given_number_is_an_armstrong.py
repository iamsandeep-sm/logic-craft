"""
Q15. Check whether the given number is an Armstrong number.
"""
number = int(input("Enter any number : "))
org_num = number
total_sum = 0
count = len(str(number))
# 153 ------- 1*1*1 + 5*5*5 + 3*3*3 == total
while number > 0:
    digit = number % 10
    total_sum += digit ** count
    number =  number // 10
if total_sum == org_num:
    print("This is an armstrong number")
else:
    print("This is not an armstrong number")
