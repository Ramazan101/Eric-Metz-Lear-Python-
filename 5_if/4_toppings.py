# requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers":
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}")
#
# print("\nFinished making your pizza!")
#
#
# requested_toppings = ["mushroom", "piperoni", "peppers"]
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

available_toppings = ["mushrooms", "olives", "green peppers",
                      "peperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

"""Программа перебирает список заказанных топпингов. Внутри цикла про-
грамма сначала проверяет, что каждый заказанный топпинг присутствует в списке
доступных топпингов"""
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("\nFinished making your pizza!")

