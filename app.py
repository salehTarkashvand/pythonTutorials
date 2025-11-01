# logical operators

#and
#or
#not

good_credit = False
high_income = True
student = False

# The `or` operator in Python is a logical operator that returns `True` if at least one
# of the conditions it connects evaluates to `True`. In your code snippet, the
# expression `good_credit or high_income` will evaluate to `True` if either
# `good_credit` is `True`, `high_income` is `True`, or both are `True`. If both
# `good_credit` and `high_income` are `False`, then the `or` expression will evaluate
# to `False`.

if good_credit or high_income:
    print("eligibale")
else:
    print("not eligibale")

# The `and` operator in Python is a logical operator that returns `True` only if both
# of the conditions it connects evaluate to `True`. In your code snippet, the
# expression `good_credit and high_income` will evaluate to `True` only if both
# `good_credit` and `high_income` are `True`. If either `good_credit` or `high_income`
# is `False`, then the `and` expression will evaluate to `False`.

if good_credit and high_income:
    print("eligibale")
else:
    print("not eligibale")

# The `not` operator in Python is a logical operator that negates the boolean value of the operand
# it precedes. In your code snippet, the expression `not student` will evaluate to `True` if
# `student` is `False`, and `False` if `student` is `True`. It essentially flips the boolean value
# of the operand.
if not student:
    print("eligibale")
else:
    print("not eligibale")

# The expression `not student and (good_credit and high_income)` is combining multiple conditions
# using logical operators in Python.
if not student and ( good_credit and high_income ):
    print("eligibale")
else:
    print("not eligibale")