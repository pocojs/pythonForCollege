products = [("Хлеб", 50), ("Молоко", 80), ("Сыр", 150), ("Яблоки", 70)]

result = sorted(products, key=lambda product: product[1], reverse=True)

print(result)