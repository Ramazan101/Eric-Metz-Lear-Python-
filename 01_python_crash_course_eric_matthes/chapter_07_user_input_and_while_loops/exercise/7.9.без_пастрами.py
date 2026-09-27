"""7.9. Без пастрами: используя список sandwich_orders из упражнения 7.8, проследите за
тем, чтобы значение 'pastrami' встречалось в списке как минимум три раза. Добавьте в на-
чало программы код для вывода сообщения о том, что пастрами больше нет, и напишите
цикл while для удаления всех вхождений 'pastrami' из sandwich_orders. Убедитесь в том,
что в finished_sandwiches значение 'pastrami' не встречается ни одного раза."""

sandwich_orders = ["сэндвич с курицей", 'pastrami', 'pastrami',"сэндвич с моёнезом ",
                   "сэндвич с шашлыком", "сэндвич с говядиной", "сэндвич с кетчупом",
                   'pastrami']
print("pastrami больше нет.")

while "pastrami" in sandwich_orders:
        sandwich_orders.remove("pastrami")
print(sandwich_orders)

