product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}

remove_keys = ["stock", "warehouse"]

for key in remove_keys:
    product.pop(key)

print(product)