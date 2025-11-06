# ==============================================================
# Python Array Module — Complete Reference and Examples
# ==============================================================

# The 'array' module provides a space-efficient way to store
# homogeneous (same-type) data — unlike Python lists, which can
# hold elements of mixed types. Arrays are useful for numeric
# computations, binary data, and low-level interfacing with C code.

from array import array

# --------------------------------------------------------------
# Example 1: Integer Array
# --------------------------------------------------------------
# 'i' → signed int (usually 4 bytes)
numbers = array('i', [1, 2, 3])
numbers[0] = 10  # update the first element
print("Example 1 - Integer Array:", numbers.tolist())  # [10, 2, 3]


# --------------------------------------------------------------
# Example 2: Float Array
# --------------------------------------------------------------
# 'f' → 4-byte floating point (single precision)
floats = array('f', [1.5, 2.7, 3.14])
floats.append(4.5)
print("Example 2 - Float Array:", floats.tolist())  # [1.5, 2.7, 3.14, 4.5]


# --------------------------------------------------------------
# Example 3: Unsigned Short Array
# --------------------------------------------------------------
# 'H' → unsigned short (2 bytes)
unsigned = array('H', [0, 100, 65000])
unsigned.append(65535)
print("Example 3 - Unsigned Short Array:", unsigned.tolist())


# --------------------------------------------------------------
# Example 4: Removing and Modifying Elements
# --------------------------------------------------------------
numbers = array('i', [5, 10, 15, 20])
numbers.pop(0)      # remove first element
numbers.insert(0, 99)  # insert new element at index 0
print("Example 4 - Modified Array:", numbers.tolist())  # [99, 10, 15, 20]


# --------------------------------------------------------------
# Example 5: Converting to a List
# --------------------------------------------------------------
# You can convert an array to a normal Python list
list_version = numbers.tolist()
print("Example 5 - Converted to List:", list_version)


# --------------------------------------------------------------
# Example 6: Accessing and Iterating Through Elements
# --------------------------------------------------------------
for value in floats:
    print("Example 6 - Iterating Float Value:", value)


# --------------------------------------------------------------
# Full List of Type Codes (for reference)
# --------------------------------------------------------------
#  Code | C Type Equivalent     | Python Type | Size (bytes) | Description
#  -----|-----------------------|--------------|---------------|-----------------------
#   'b' | signed char           | int          | 1             | 8-bit integer (signed)
#   'B' | unsigned char         | int          | 1             | 8-bit integer (unsigned)
#   'h' | signed short          | int          | 2             | 16-bit integer (signed)
#   'H' | unsigned short        | int          | 2             | 16-bit integer (unsigned)
#   'i' | signed int            | int          | 2 or 4        | Normal integer (signed)
#   'I' | unsigned int          | int          | 2 or 4        | Normal integer (unsigned)
#   'l' | signed long           | int          | 4             | Long integer (signed)
#   'L' | unsigned long         | int          | 4             | Long integer (unsigned)
#   'q' | signed long long      | int          | 8             | 64-bit integer (signed)
#   'Q' | unsigned long long    | int          | 8             | 64-bit integer (unsigned)
#   'f' | float                 | float        | 4             | 32-bit float
#   'd' | double                | float        | 8             | 64-bit double precision float

# --------------------------------------------------------------
# Key Takeaways:
# --------------------------------------------------------------
# - Use the 'array' module when you need efficient numeric storage.
# - Arrays can only store one data type (defined by the type code).
# - You can append(), insert(), pop(), and iterate through arrays.
# - Convert arrays to lists with .tolist() when needed.
# ==============================================================

