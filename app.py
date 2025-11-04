# list unpack

list = [1, 2, 3]
a, b, c = list

print(a, b, c)  # 1 2 3


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, b, *c = numbers

print(a, b, c)  # 1 2 [3, 4, 5, 6, 7, 8, 9]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, *c, b = numbers

print(a, b, c)  # 1 9 [2, 3, 4, 5, 6, 7, 8]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, *c, b, d = numbers

print(a, b, c, d)  # 1 8 [2, 3, 4, 5, 6, 7] 9
