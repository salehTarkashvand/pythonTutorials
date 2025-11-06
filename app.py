# zip() method

# zip() takes two or more iterables (like lists or tuples) and pairs their elements together into tuples.

item1 = [1, 2, 3]
item2 = [10, 20, 30]

result = list(zip(item1, item2, "abc"))
print(result)  # [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]
