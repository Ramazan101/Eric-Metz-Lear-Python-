# Iskak words
cars = ["Chevrolet", "Ford", "Mclaren", "Brabus", "Bentlie", "Cadillac", "Volvo", "ChanGan", "LI", "Xiaomi", "Corvet"]
cars.sort(reverse=True)
print(cars)
cars.sort(reverse=False)
print(cars)
cars.reverse()#Обратите внимание: метод reverse() не сортирует элементы в обратном алфавитном порядке, а просто переходит к обратному порядку списка:
print(cars)
cars.reverse()


"""Временная сортировка списка функцией sorted()"""

cars = ["bmv", "audi", "toyota", "subaru"]

print("Here is original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

