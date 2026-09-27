"""УПРАЖНЕНИЯ
5.1. Проверка условий: напишите последовательность условий. Выведите описание каж-
дой проверки и ваш прогноз относительно ее результата. Код должен выглядеть примерно
так:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Внимательно просмотрите результаты. Убедитесь в том, что вы понимаете, почему
результат каждой строки равен True или False.
• Создайте как минимум 10 условий. Не менее пяти одних должны давать результат
True, а не менее пяти других — результат False."""

car = "subaru"
print("Is car == 'subaru'? I predict True")
bool_car = car == "subaru"
print(bool_car)
print("\nIs car == 'bmv'? I predict False")
bool_car = car == "bmv"
print(bool_car)