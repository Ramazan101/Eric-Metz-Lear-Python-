"""8.3. Футболка: напишите функцию make_shirt(), которая получает размер футболки
и текст, который должен быть напечатан на ней. Функция должна выводить сообщение
с размером и текстом.
Вызовите функцию с использованием позиционных аргументов. Вызовите функцию во
второй раз с использованием именованных аргументов."""

def make_shirt(size_c=int, text_c=str):
    print(f"Размер футболки {size_c} и текст на нем {text_c}")
make_shirt(42, "hello world!")
make_shirt(size_c=32, text_c="hello world")


"""8.4. Большие футболки: измените функцию make_shirt(), чтобы по умолчанию футболки
имели размер L и на них выводился текст «I love Python». Создайте футболку с размером L
и текстом по умолчанию, а также футболку любого размера с другим текстом."""

def make_shirt(text_c, size_c="'L'"):
    print(f"Size {size_c} and text {text_c}")
make_shirt("I love python!\n")


def make_shirt(size_c, text_c = "I love Python"):
    print(f"Size: {size_c}\nText: {text_c}")
make_shirt(size_c="'XL'")
make_shirt(size_c="'X'", text_c="I love Rust\n")

"""8.5. Города: напишите функцию describe_city(), которая получает названия города
и страны. Функция должна выводить простое сообщение (например, «Reykjavik is in
Iceland»). Задайте параметру страны значение по умолчанию. Вызовите свою функцию
для трех разных городов, по крайней мере один из которых не находится в стране по
умолчанию."""

def describe_city(name_city, name_country = "Russia"):
    print(f"{name_city.title()} is in {name_country.title()}.")
describe_city("moscow")
describe_city("irkutsk")
describe_city("bishkek", "kyrgyzstan")