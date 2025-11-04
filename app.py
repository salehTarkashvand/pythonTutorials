# sorting list 

# sort()
numbers = [3, 4, 1, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

# sorted()
numbers = [3, 4, 1, 2]
print(sorted(numbers))  # [1, 2, 3, 4]
print(numbers)  # [3, 4, 1, 2]


# handle with function for tuples

products = [("product1", 12), ("product1", 9), ("product1", 55)]


def sort_item(item):
    return item[1]


products.sort(key=sort_item)
print(products)  # [('product1', 9), ('product1', 12), ('product1', 55)]


# handle with lambda for tuples
products = [("product1", 12), ("product1", 9), ("product1", 55)]

products.sort(key=lambda item: item[1])
print(products)  # [('product1', 9), ('product1', 12), ('product1', 55)]
