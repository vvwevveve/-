prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
total_price = sum(prices)
average_price = total_price / len(prices)

print(f"самый дорогой товар: {max_price}")
print(f"самый дешевый товар: {min_price}")
print(f"общая стоимость всех товаров: {total_price}")
print(f"средняя цена товара: {average_price}")