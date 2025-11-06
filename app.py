# Filtered and maping list with comprehension


products = [("product1", 12), ("product1", 9), ("product1", 55)]

filtred_product = list(filter(lambda product: product[1] >= 10, products))
# Filtered list comprehension
filter = [product for product in products if product[1]>= 10 ]

map_product = list(filter(lambda product: product[1], products))
# Mapping list comprehension
map = [item[1] for item in products ]

print(filtred_product)