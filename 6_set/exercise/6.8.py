"""6.8. Домашние животные: создайте несколько словарей, имена которых представляют
клички домашних животных. В каждом словаре сохраните информацию о виде животно-
го и имени владельца. Сохраните словари в списке с именем pets. Переберите элементы
списка. В процессе перебора выведите всю имеющуюся информацию о каждом животном."""


lion = {
    "type_animal": "dog",
    "owner_name": "anarbek"
}

kanchuk = {
    "type_animal": "dog",
    "owner_name": "janulai"
}

marush = {
    "type_animal": "cat",
    "owner_name": "me"
}

pets = [lion, kanchuk, marush]

for pet in pets:
    owner_name = f"Owner name: {pet["owner_name"]}."
    print(owner_name)
    print(f"\tType animal: {pet["type_animal"]}.")
