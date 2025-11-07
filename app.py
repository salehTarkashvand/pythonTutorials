# =============================================
# Python Exception Handling — Full Examples
# Author: Saleh Torkashvand
# =============================================

# This script demonstrates many built-in exception types in Python,
# how they occur, and how to handle them using try / except / else / finally.

# ------------------------------------------------------------
# 1️⃣ ValueError — invalid value for a valid type
# ------------------------------------------------------------
try:
    num = int("abc")
except ValueError as ex:
    print("ValueError:", ex)  # Output: ValueError: invalid literal for int() with base 10: 'abc'

# ------------------------------------------------------------
# 2️⃣ TypeError — invalid operation between incompatible types
# ------------------------------------------------------------
try:
    result = "3" + 5
except TypeError as ex:
    print("TypeError:", ex)  # Output: can only concatenate str (not "int") to str

# ------------------------------------------------------------
# 3️⃣ NameError — using an undefined variable
# ------------------------------------------------------------
try:
    print(unknown_variable)
except NameError as ex:
    print("NameError:", ex)  # Output: name 'unknown_variable' is not defined

# ------------------------------------------------------------
# 4️⃣ IndexError — index out of range
# ------------------------------------------------------------
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as ex:
    print("IndexError:", ex)  # Output: list index out of range

# ------------------------------------------------------------
# 5️⃣ KeyError — accessing a missing key in a dictionary
# ------------------------------------------------------------
try:
    person = {"name": "Saleh"}
    print(person["age"])
except KeyError as ex:
    print("KeyError:", ex)  # Output: 'age'

# ------------------------------------------------------------
# 6️⃣ ZeroDivisionError — dividing by zero
# ------------------------------------------------------------
try:
    x = 10 / 0
except ZeroDivisionError as ex:
    print("ZeroDivisionError:", ex)  # Output: division by zero

# ------------------------------------------------------------
# 7️⃣ FileNotFoundError — file does not exist
# ------------------------------------------------------------
try:
    file = open("nonexistent.txt")
except FileNotFoundError as ex:
    print("FileNotFoundError:", ex)  # Output: [Errno 2] No such file or directory

# ------------------------------------------------------------
# 8️⃣ AttributeError — accessing an invalid attribute
# ------------------------------------------------------------
try:
    "hello".append("world")
except AttributeError as ex:
    print("AttributeError:", ex)  # Output: 'str' object has no attribute 'append'

# ------------------------------------------------------------
# 9️⃣ ImportError / ModuleNotFoundError
# ------------------------------------------------------------
try:
    import not_a_real_module
except ModuleNotFoundError as ex:
    print("ModuleNotFoundError:", ex)  # Output: No module named 'not_a_real_module'

# ------------------------------------------------------------
# 🔟 AssertionError — assert statement fails
# ------------------------------------------------------------
try:
    assert 2 + 2 == 5
except AssertionError as ex:
    print("AssertionError:", ex)  # Output: AssertionError

# ------------------------------------------------------------
# 1️⃣1️⃣ OSError — general OS-level error
# ------------------------------------------------------------
try:
    open("/root/protected.txt", "r")
except OSError as ex:
    print("OSError:", ex)  # Output: [Errno 13] Permission denied

# ------------------------------------------------------------
# 1️⃣2️⃣ RecursionError — too much recursion
# ------------------------------------------------------------
def recurse():
    return recurse()
try:
    recurse()
except RecursionError as ex:
    print("RecursionError:", ex)  # Output: maximum recursion depth exceeded

# ------------------------------------------------------------
# 1️⃣3️⃣ OverflowError — number too large to represent
# ------------------------------------------------------------
import math
try:
    math.exp(1000)
except OverflowError as ex:
    print("OverflowError:", ex)  # Output: math range error

# ------------------------------------------------------------
# 1️⃣4️⃣ MemoryError — not enough memory (simulated example)
# ------------------------------------------------------------
try:
    x = [0] * (10**9 * 10)
except MemoryError as ex:
    print("MemoryError:", ex)  # Output: MemoryError

# ------------------------------------------------------------
# 1️⃣5️⃣ RuntimeError — generic runtime error
# ------------------------------------------------------------
try:
    raise RuntimeError("Something unexpected happened")
except RuntimeError as ex:
    print("RuntimeError:", ex)  # Output: Something unexpected happened

# ------------------------------------------------------------
# 1️⃣6️⃣ EOFError — no input when expected
# ------------------------------------------------------------
try:
    # Uncomment to test manually in terminal
    # input()  # Press Ctrl+D or EOF to trigger
    pass
except EOFError as ex:
    print("EOFError:", ex)

# ------------------------------------------------------------
# 1️⃣7️⃣ Exception — catch-all handler for unknown exceptions
# ------------------------------------------------------------
try:
    risky = 10 / 0
except Exception as ex:
    print("Generic Exception caught:", type(ex), ex)

# ------------------------------------------------------------
# ✅ finally — runs no matter what happens
# ------------------------------------------------------------
try:
    print("Trying to divide...")
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block always runs!")  # Output: This block always runs!

# ------------------------------------------------------------
# ✅ else — runs only if no exception happens
# ------------------------------------------------------------
try:
    print("Trying with valid input:")
    num = int("25")
except ValueError:
    print("Invalid input.")
else:
    print("No exceptions were thrown.")  # Output: No exceptions were thrown.
    print("Your age is", num)
