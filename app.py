# Conditions and If statements

# syntax if statement

#if Conditions:
#    Operation
#elif Conditions:
#    Operation
#elif Conditions:
#    Operation
#else:
#    Operation


# This code snippet is using conditional statements to determine the appropriate message to print
# based on the value of the `temperature` variable. Here's a breakdown of the logic:

temprature = 35
# `if temperature > 30:` is a conditional statement that checks if the value stored in the
# `temperature` variable is greater than 30. If this condition is true, the code block under this `if`
# statement will be executed, which in this case is printing "it's warm" and "drink water".
if temprature > 30:
    print("it`s warm")
    print("drink water")

# `elif temperature > 20:` is an "else if" statement that checks if the value stored in the
# `temperature` variable is greater than 20. If the previous `if` condition (temperature > 30) is not
# met, this `elif` condition is evaluated. If the temperature is greater than 20 but not greater than
# 30, the code block under this `elif` statement will be executed, which in this case is printing
# "it's nice".
elif temprature > 20:
    print("it`s nice")

# The `else:` statement in Python is used as a catch-all condition that executes when none of the
# preceding `if` or `elif` conditions are true. In the context of the code snippet you provided, if
# the temperature is not greater than 30 and not greater than 20, then the `else:` block will be
# executed, which prints "it's cold".
else:
    print("it`s cold")