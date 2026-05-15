stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}

min_key = min(stock, key=stock.get)

print(min_key)