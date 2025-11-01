# short circuit


good_credit = False
high_income = True
student = False

# What is short circuit in Python?
# The OR operator returns TRUE when either of the relations or operands in the expression evaluates to true.
# Short-circuiting in Python is a technique by which execution of boolean expression containing 'or' and 'and' operator in Python is halted as soon as the truth value of the expression is determined

if student and good_credit and high_income:
    print("eligibale")
else:
    print("not eligibale")
