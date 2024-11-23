text = "яблоко груша яблоко апельсин груша груша"

fruit_dict = {
    "яблоко": 0,
    "груша": 0,
    "апельсин": 0
}

text_list = text.split()

for i in text_list:
    fruit_dict[i] = fruit_dict.get(i, 0) + 1


print(fruit_dict)
