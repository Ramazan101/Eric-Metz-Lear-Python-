"""7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями раз-
личных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле
переберите элементы первого списка и выведите сообщение для каждого элемента (напри-
мер, «I made your tuna sandwich»). После этого каждый сэндвич из первого списка пере-
мещается в список finished_sandwiches. После того как все элементы первого списка будут
обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей."""

sandwich_orders = ["сэндвич с курицей", "сэндвич с моёнезом ", "сэндвич с шашлыком", "сэндвич с говядиной", "сэндвич с кетчупом"]
finished_sandwich = []

while sandwich_orders:
    popping_sandwich = sandwich_orders.pop()
    print(f"I made your {popping_sandwich}.")
    finished_sandwich.append(popping_sandwich)


print("\nСписок всех изготовленных сэндвичей.")
for sandwich in finished_sandwich:
    print(sandwich)
