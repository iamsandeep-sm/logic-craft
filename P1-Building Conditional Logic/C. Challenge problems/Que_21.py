
# ? Check whether a number is a palindrome of 3 digits without loops.

def is_palindrome(num):
    str_num = str(num)

    reversed_num = str_num[::-1]
    return str_num == reversed_num

print(is_palindrome(161))
print(is_palindrome(12921))