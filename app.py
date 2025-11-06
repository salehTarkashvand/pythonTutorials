# filtered a list


products = [("product1", 12), ("product1", 9), ("product1", 55)]

filtred_product = list(filter(lambda product: product[1] >= 10, products))

print(filtred_product)