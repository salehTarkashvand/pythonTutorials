# calling a function with argument unpacking (*args)


def multiply(*numbers):
    print(numbers)  # (1, 2, 3, 4, 10)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 10))  # 240
