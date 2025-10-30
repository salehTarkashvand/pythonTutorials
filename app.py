course = "python programming"  # string methods

# The code `print(len(course))` is calculating the length of the string variable `course` and then
# printing out that length. In this case, the length of the string "python programming" is calculated
# and printed to the console.
print(len(course))

# The `course.upper()` method is converting all the characters in the `course` string to
# uppercase letters. It does not modify the original string `course`, but returns a new string
# with all characters in uppercase.
print(course.upper())

# The `course.lower()` method is converting all the characters in the `course` string to
# lowercase letters. It does not modify the original string `course`, but returns a new string
# with all characters in lowercase.
print(course.lower())

# The `course.title()` method is converting the string `course` into title case. This means that
# the first letter of each word in the string will be capitalized, while all other letters will
# be in lowercase. It does not modify the original string `course`, but returns a new string
# with the title case formatting applied.
print(course.title())

# The `course.strip()` method is removing any leading or trailing whitespace characters from the
# string `course`. It does not modify the original string `course`, but returns a new string
# with the leading and trailing whitespace removed.
print(course.strip())

# The `course.find("pr")` method is searching for the substring "pr" within the `course` string.
# If the substring is found, it returns the index of the first occurrence of the substring
# within the string. If the substring is not found, it returns -1. In this case, it is searching
# for the substring "pr" in the string "python programming" and will return the index where "pr"
# starts, which is 7.
print(course.find("pr"))

# The expression `"pro" in course` is checking if the substring "pro" is present within the
# string `course`. It returns a boolean value, `True` if the substring is found in the string,
# and `False` if it is not found. In this case, it is checking if "pro" is a substring of
# "python programming" and will return `True` because "pro" is indeed present in the string.
print("pro" in course)

# The expression `"pro" not in course` is checking if the substring "pro" is not present within
# the string `course`. It returns a boolean value, `True` if the substring is not found in the
# string, and `False` if it is found. In this case, it is checking if "pro" is not a substring
# of "python programming" and will return `False` because "pro" is indeed present in the string.
print("pro" not in course)
