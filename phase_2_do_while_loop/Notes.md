# STUDY NOTE: Do-While Loop in Python

- Python does NOT have a 'do-while' keyword or curly braces { }.
- Instead, we use 'while True:' so the code runs at least once.
- We put 'if condition: break' at the bottom to exit the loop.

>Normally, a while loop checks its condition before running the code. If the condition is false right away, the loop never runs.
A do-while loop flips this:
1. DO the action at least once.
2. WHILE the condition is true, repeat it.

How to Write It in Python

>To build this in Python, you create a loop that runs forever (while True:) and put the stop condition at the very bottom using if and break.

--> To see the working code-
[Click here to open the working Python code](q01_keep_taking_numbers_from_the_user_until_0_is.py)