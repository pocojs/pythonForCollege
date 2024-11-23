data = {}
for i in range(3):
    user_product = input("Введите название продукта: ")
    user_price = int(input("Введите его стоимость: "))
    data[user_product] = user_price

buy_product = input("Какой продукт вы хотите купить? ")

product_price = data.get(buy_product)

if buy_product in data:
    print(f"Стоимость {buy_product}: {product_price}")
else:
    print("Продукт не найден")

