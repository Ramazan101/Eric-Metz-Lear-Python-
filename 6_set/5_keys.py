"""Перебор всех ключей в словаре"""
favorite_languages = {
    "shasha": "c",
    "ramadan": "python",
    "alialbarakat": "rubi",
    "silvana": "c",
    "obsidian": "js",
}

if "eric" not in favorite_languages.keys():
    print("Eric please take our poll!\n")
# перебор всех ключей в словаре
# for key in favorite_languages.keys():
#     print(key.title())

friends = ["shasha", "silvana"]
for key in favorite_languages.keys():
    print(key.title())

    if key in friends:
        language = favorite_languages[key].title()
        print(f"\t{key.title()}, I see you love {language}")

"""sorted keys"""

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thanks for talking the poll!")
