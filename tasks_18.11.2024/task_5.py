products = [("Бананы", 120), ("Мясо", 300), ("Яблоки", 80), ("Сыр", 200), ("Молоко", 50)] 

more_hundred = filter(lambda price: price[1] > 100, products)

list_expen = list(map(lambda expen: expen[0], more_hundred))

print(list_expen)

