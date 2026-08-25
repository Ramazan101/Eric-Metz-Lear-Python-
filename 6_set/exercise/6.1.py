"""УПРАЖНЕНИЯ
6.1. Человек: используйте словарь для сохранения информации об известном вам челове-
ке. Сохраните имя, фамилию, возраст и город, в котором живет этот человек. Словарь дол-
жен содержать ключи с такими именами, как first_name, last_name, age и city. Выведите
каждый фрагмент информации, хранящийся в словаре."""

famous_person = {
    "first_name": "Johnny",
    "last_name": "Depp",
    "age": 63,
    "city": "Owenborough",
}
print(famous_person["first_name"])
print(famous_person["last_name"])
print(famous_person["age"])
print(famous_person["city"])

# for key, value in famous_person.items():
#     print(value)
