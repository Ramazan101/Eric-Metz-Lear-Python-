"""3.8. Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать.
• Сохраните названия стран в списке. Проследите за тем, чтобы список не хранился
в алфавитном порядке.
• Выведите список в исходном порядке. Не беспокойтесь об оформлении, просто выведите его как обычный список Python.
• Используйте функцию sorted() для вывода списка в алфавитном порядке без изменения списка.
• Снова выведите список, чтобы показать, что он по-прежнему хранится в исходном
порядке.
• Используйте функцию sorted() для вывода списка в обратном алфавитном порядке
без изменения порядка исходного списка.
• Снова выведите список, чтобы показать, что исходный порядок не изменился.
• Измените порядок элементов вызовом reverse(). Выведите список, чтобы показать,
что элементы следуют в другом порядке.
• Измените порядок элементов повторным вызовом reverse(). Выведите список, чтобы показать, что список вернулся к исходному порядку.
• Отсортируйте список в алфавитном порядке вызовом sort(). Выведите список, чтобы показать, что элементы следуют в другом порядке.
• Вызовите sort() для перестановки элементов списка в обратном алфавитном порядке. Выведите список, чтобы показать, что порядок элементов изменился.
"""

name_country = ["Island", "Greece", "China"]
anara_country = ["Japan", "South Korea",  "Italy"]
alvina_country = ["France", "Turkey", "Korea", "USA"]
argen_country = ["America", "German", "Japan"]
ashirov_c = ["South Korea",
             "Dubai",
             "Malaysia"]
nursultan_c = ["Brazil", "Vietnam", "Polish", "Egypt", "Nigeria"]
all_c = name_country + anara_country + alvina_country + argen_country + ashirov_c + nursultan_c
print(f"\nQuantity country: {len(all_c)}")
print(f"\nAll countries: {all_c}")
print(f"\nВывода списка в алфавитном порядке: {sorted(all_c)}")
print(f"\nПо-прежнему хранится в исходном порядке: {all_c}")
all_c.reverse()
print(f"\nИзмененный порядок элементов вызовом reverse(): {all_c}")
all_c.sort()
print(all_c)
all_c.sort(reverse=True)
print(all_c)

# all_country = (
#     f"Страны где хочет побывать Искак: {", ".join(name_country)}.\n"
#     f"Страны где хочет побывать Анара: {", ".join(anara_country)}.\n"
#     f"Страны где хочет побывать Алвина: {", ".join(alvina_country)}.\n"
#     f"Страны где хочет побывать Argen: {", ".join(argen_country)}"
# )
# print(all_country)
#
#
# name = ["a", "t", "b"]
# join_c = ", ".join(name)
# print(join_c)


"""3.9. Количество гостей: в одной из программ из упражнений с 3.4 по 3.7 используйте len()
для вывода сообщения с количеством людей, приглашенных на обед."""

more_person = ["Elon Musk", "Justin Timberlake", "Taylor Swift", "Buzz Dam Tatiana", "Bruno Mars\n"]
print(len(more_person))


"""3.10. Все функции: придумайте информацию, которую можно было бы хранить в списке.
Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно. Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
упоминавшуюся в этой главе, хотя бы один раз."""



countries = ["Japan", "Italy", "China", "France"]
print(f"Страны до обновления {countries}")
countries.insert(0, "Turkey")
countries.append("Egypt")
print(f"Страны после обновления {countries}")



print(f"\nОтсортированный список(временно): {sorted(countries)}")
print(f"Оригинал остался прежним {countries}")


countries.reverse()
print(f"\nРазвернутый список: {countries}")


countries.sort()
print(f"\nОтсортированный по алфавиту {countries}")


countries.sort(reverse=True)
print(f"\nОтсортированный в противоположном порядке алфавита {countries}")


print(f"\nВсе страны который есть в списке: {len(countries)}")



del countries[0]
print(f"\nСписок после удаления countries[0]: {countries}")

popped_country = countries.pop()
print(f"\nИзвлекли страну через pop(): {popped_country}")
print(f"Список после удаления страны через pop(): {countries}")

countries.remove("Japan")
print(f"\nСписок после удаления через remove('Japan'): {countries}")






