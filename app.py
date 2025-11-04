# Transforming a list

# transform with for operator

products = [("product1", 12), ("product1", 9), ("product1", 55)]

prises = []
for item in products:
    prises.append(item[1])

print(prises)  # [12, 9, 55]


# transform with map() function


products = [("product1", 12), ("product1", 9), ("product1", 55)]

x = list(map(lambda item: item[1], products))


print(x)  # [12, 9, 55]
