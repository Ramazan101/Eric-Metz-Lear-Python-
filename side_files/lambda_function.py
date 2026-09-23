# add = lambda a, b: a + b
# print(add(1, 2))
#
# double = lambda a, b: a * b
# print(double(23, 2))
#
# is_even = lambda number: number % 2 == 0
# print(is_even(5))
#
# print(is_even(4))
#
# def square(number) -> int:
#     return number ** 2
#
#
# square_lambda = lambda number= int: number ** 2
# print(square_lambda(2))

# Пример 1; увеличение каждого число на 1
# numbers = [1, 2, 3]
# result = list(map(lambda number: number + 1, numbers))
# print(result)
#
# # Пример 2; умножение каждое число на 2
# numbers = [1, 2, 3, 4, 5]
#
# result = list(map(lambda number: number * 2, numbers))
# print(result)
#
# # Пример 3: сделать слова заглавными
# names = ["bob", "alex", "tom"]
# result = tuple(map(str.upper, names))
# print(result)
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# squares = []
#
# for number in numbers:
#     squares.append(number ** 2)
# print(squares)
#
#
# squares = list(map(lambda number: number ** 2, numbers))
# print(squares)
#
#
# def double(number):
#     return number * 2
# numbers = list(map(double, numbers))
# print(double(12))

# text = input("Напиши любое число: ")
# numbers = list(map(int, text.split()))
# print(numbers)
#
# def check(number):
#     return number > 5
# numbers = [2, 4, 6, 8]
# result = list(filter(check, numbers))
# print(result)

# filter() нужен, чтобы ОСТАВИТЬ только подходящие элементы.
# names = ["Bob", "Alexandra", "Tom"]
# result = list(filter(lambda name: len(name) > 4, names))

# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = []
# for number in numbers:
#     if number % 2 == 0:
#         result.append(number)
#
# print(result)

# Теперь filter():
# result = list(filter(lambda number:
#                      number % 2 == 0, numbers))
# print(result)

# numbers = [3, 4, 12, 34, 5, 23, 1, 6, 7]
# result = list(filter(lambda number: number > 10, numbers))
# print(result)
#
# names = ["Alex", "Askar", "Bob", "Alexander", "Tom"]
# result = list(filter(lambda name: len(name) > 4, names))
# print(result)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# even_numbers = list(
#     filter(lambda number: number % 2 == 0, numbers)
# )
# print(even_numbers)
#
# squares = list(
#     map(lambda number: number ** 2, even_numbers)
# )
# print(squares)
#
# names = ["bob", "alex"]
# ages = [20, 25]
#
# result = list(zip(names, ages))
#
# print(result)
#
products = ["mouse", "keyboard"]
prices = [120, 140]

for product, price in zip(products, prices):
    print(product, price)

