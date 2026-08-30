"""6.9. Любимые места: создайте словарь с именем favorite_places. Придумайте названия
трех мест, которые станут ключами словаря, и сохраните для каждого человека от одного
до трех любимых мест. Чтобы задача стала более интересной, опросите нескольких друзей
и соберите реальные данные для своей программы. Переберите данные в словаре, выведите
имя каждого человека и его любимые места."""

favorite_places = {
    "maxim": ["egypt", "japan",  "germany"],
    "anna": ["dubai", "uzbekistan", "canada"],
    "roman": ["china", "kenya", "kyrgyzstan"]
}

for names, places in favorite_places.items():
    print(f"Favorite places chosen {names.title()} this:")
    for place in places:
        print(f"* {place.title()}")
