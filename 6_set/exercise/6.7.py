"""6.7. Люди: начните с программы, написанной для упражнения 6.1 (с. 113). Создайте два но-
вых словаря, представляющих разных людей, и сохраните все три словаря в списке с име-
нем people. Переберите элементы списка людей. В процессе перебора выведите всю имею-
щуюся информацию о каждом человеке."""

# Создаем 3 словaря описывающий известного человека
person_1 = {
    "first_name": "Johnny",
    "last_name": "Depp",
    "age": 63,
    "city": "Owensboro",
}

person_2 = {
    "first_name": "Keanu",
    "last_name": "Reeves",
    "age": 61,
    "city": "Beirut",
}

person_3 = {
    "first_name": "Angelina",
    "last_name": "Jolie",
    "age": 51,
    "city": "Los Angeles",
}
# Сохраняем все словари в список
people = [person_1, person_2, person_3]

# Перебираем список людей и выводим информацию о каждом
for person in people:
    full_name = f"{person["first_name"]} {person["last_name"]}"
    print(f"Full name: {full_name}")
    print(f"\tAge: {person["age"]} years old.")
    print(f"\tCity: {person["city"]}.")