"""6.11. Города: создайте словарь с именем cities. Используйте названия трех городов в ка-
честве ключей словаря. Создайте словарь с информацией о каждом городе; включите в него
страну, в которой расположен город, примерную численность населения и один примеча-
тельный факт, относящийся к этому городу. Ключи словаря каждого города должны назы-
ваться country, population и fact. Выведите название каждого города и всю сохраненную
информацию о нем."""

cities = {
    "Moscow": {
        "country": "Russia",
        "population": "13.1 million",
        "fact": "It is the northernmost and coldest megacity on Earth."
    },
    "Shanghai": {
        "country": "China",
        "population": "24.1 million",
        "fact": "It features the world's longest metro system and the fastest commercial maglev train."
    },
    "Lagos": {
        "country": "Nigeria",
        "population": "16.6 million",
        "fact": "It is a major financial hub in Africa and is famous for its floating city of Makoko."
    }
}

for city, facts in cities.items():
    print(f"\nName city: {city}.")
    print(f"\tCountry: {facts["country"].title()}.\n\t"
          f"Population: {facts["population"]}.\n\t"
          f"Fact: {facts["fact"]}")
