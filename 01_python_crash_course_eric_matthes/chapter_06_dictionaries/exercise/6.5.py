"""6.5. Реки: создайте словарь с названиями трех больших рек и стран, по которым протекает
каждая река. Одна из возможных пар «ключ-значение» — 'nile': 'egypt'.
• Используйте цикл для вывода сообщения с упоминанием реки и страны — напри-
мер, «The Nile runs through Egypt».
• Используйте цикл для вывода названия каждой реки, включенной в словарь.
• Используйте цикл для вывода названия каждой страны, включенной в словарь."""


rivers = {
    "amazon": "argentina",
    "naryn":  "kyrgyzstan",
    "kongo": "kongo",
    'nile': 'egypt',
    "yangtze": "china",
}
# Используйте цикл для вывода сообщения с упоминанием реки и страны.
for river, country in rivers.items():
    print(f"The {river.title()} runs {country.title()}.")

# Используйте цикл для вывода названия каждой реки, включенной в словарь.
for river in rivers.keys():
    print(f"The {river.title()} river.")
print("\n")

# Используйте цикл для вывода названия каждой страны, включенной в словарь.
for country in rivers.values():
    print(f"The {country.title()} country.")
