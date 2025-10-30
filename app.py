# Type conversion

## The `int()` function in Python is used for type conversion, specifically for converting a value to
# an integer data type. In the code snippet you provided, `int(x)` is converting the input value
# stored in the variable `x` (which is initially a string due to the `input()` function) into an
# integer. This allows you to perform mathematical operations or comparisons that require integer
# values.
int()
## The `float()` function in Python is used for type conversion, specifically for converting a value
# to a floating-point number data type. Similar to `int()`, `float()` allows you to convert values to
# floating-point numbers, which are numbers that have a decimal point. This conversion is useful when
# you need to perform operations or comparisons that involve decimal values.
float()
## The `bool()` function in Python is used for type conversion, specifically for converting a value to
# a boolean data type. When you pass a value to the `bool()` function, it will return `True` if the
# value is considered "truthy" and `False` if the value is considered "falsy" based on Python's truth
# value testing rules.

#falsy => 0 , "" , none
#truthy => 1 , "abc" , -2

bool()
# The `str()` function in Python is used for type conversion, specifically for converting a value to a
# string data type. When you pass a value to the `str()` function, it will convert that value into a
# string representation. This is useful when you need to concatenate strings, display values as text,
# or perform operations that require string manipulation.
str()



# The `input("x = ")` function is displaying a prompt message "x = " to the user and waiting for
# the user to enter some input. The input entered by the user will be stored in the variable `x`.
x = input("x = ")


print(# The `type(x)` function in Python is used to determine the data type of the variable `x`. When
# `type(x)` is called, it returns the type of the value stored in the variable `x`. This is
# helpful for understanding the nature of the data stored in a variable and can be used for type
# checking or debugging purposes.
type(x))

x = int(x)

print(type(x))

y = x + 1

print (f"x ={x} y={y}")