responses = {}


# Установка флага продолжения опроса.
polling_activate = True

while polling_activate:
    # Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Ответ сохраняется в словаре:
    responses[name] = response

    # Проверка продолжение опроса.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_activate = False
print("\n--Pool Results--")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


