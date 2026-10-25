
# ? Given four numbers, print them in ascending order using only if statements.

numbers = [12, 22, 10, 15]
print(f"Thr original numbers in original sequence : {numbers}")

# Pass 1: Move the largest numbers toward the right
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

if numbers[1] > numbers[2]:
    numbers[1], numbers[2] = numbers[2], numbers[1]

if numbers[2] > numbers[3]:
    numbers[2], numbers[3] = numbers[3], numbers[2]
print(f"see how was the order after pass 1  {numbers}")

# Pass 2: Clean up the remaining out-of-order numbers
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

if numbers[1] > numbers[2]:
    numbers[1], numbers[2] = numbers[2], numbers[1]
print(f"see how was the order after pass 2  {numbers}")

# Pass 3: Final check for the first two positions
if numbers[0] > numbers[1]:
    numbers[0], numbers[1] = numbers[1], numbers[0]

# Print the final sorted list
print("Ascending order:", numbers)
