
# ? Grade calculator: read marks out of 100 and print the grade (A, B, C, D, F).

marks = int(input("Enter your marks: "))
if marks >=90:
    print("You have got A grade")
elif marks >=80 and marks<90:
    print("You have got a B grade")
elif marks >=70 and marks<80:
    print("You have got a C grade")
elif marks >=60 and marks<70:
    print("You have got a D grade")
elif marks < 60 and marks >40:
    print("You have scored E grade need to work hard")
else:
    print("you have scored F, you are fail")

