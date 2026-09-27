"""8.6. Названия городов: напишите функцию city_country(), которая получает название го-
рода и страну. Функция должна возвращать строку в формате "Santiago, Chile". Вызовите
свою функцию по крайней мере для трех пар «город — страна» и выведите возвращенное
значение."""
print("Задание 8.6")
def city_country(city_name: str, country_name: str):
    return f"{city_name},{country_name}".title()

print(city_country("bishkek", "kyrgyzstan"))
print(city_country("astana", "kazakhstan"))
print(city_country("tashkent", "uzbekistan"))


"""8.7. Альбом: напишите функцию make_album(), которая строит словарь с описанием му-
зыкального альбома. Функция должна получать имя исполнителя и название альбома
и возвращать словарь, содержащий эти два вида информации. Используйте функцию
для создания трех словарей, представляющих разные альбомы. Выведите все возвращае-
мые значения, чтобы показать, что информация правильно сохраняется во всех трех сло-
варях.
Добавьте в make_album() дополнительный параметр для сохранения количества дорожек
в альбоме, имеющий значение по умолчанию None. Если в строку вызова включено значе-
ние количества дорожек, добавьте это значение в словарь альбома. Создайте как минимум
один новый вызов функции с передачей количества дорожек в альбоме."""
print("\nЗадание 8.7")
def make_album(artist_name, name_album, tracks=None):
    seen = {"artist name": artist_name,
            "name album": name_album}
    if tracks:
        seen["tracks"] = tracks
    return seen

print(make_album(artist_name="Justin Timberlake", name_album="Cry Me a River"))
print(make_album(artist_name="Justin Biber", name_album="Company"))
print(make_album(artist_name="Michael Jackson", name_album="Billy Jean"))

print(make_album("Pink Floyd", "The Dark Side Of The Moon", 50))

"""8.8. Пользовательские альбомы: начните с программы из упражнения 8.7. Напишите цикл
while, в котором пользователь вводит исполнителя и название альбома. Затем в цикле вы-
зывается функция make_album() для введенных пользователей и выводится созданный сло-
варь. Не забудьте предусмотреть признак завершения в цикле while."""

def make_album(artist_name, name_album, tracks=None):
    seen = {"artist name": artist_name,
            "name album": name_album}
    if tracks:
        seen["tracks"] = tracks
    return seen

print("\nПросим написать ваш любимый артист и его альбомы:")
while True:
    print("Напишите букву 'q' для заершении опроса.")
    a_name = input("Artist name: ")
    if a_name.lower() == "q":
        break
    album_n = input("Album name: ")
    if album_n.lower() == "q":
        break
    tracks_input = input("Tracks (нажмите Enter, если хотите пропустить): ")
    if tracks_input.lower() == "q":
        break

    tracks = int(tracks_input) if tracks_input.isdigit() else None
    formatted_name = make_album(a_name, album_n, tracks)
    print(f"Your album is: {formatted_name}")
