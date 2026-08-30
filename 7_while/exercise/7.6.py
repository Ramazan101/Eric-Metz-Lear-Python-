"""7.6. Три выхода: напишите альтернативную версию упражнения 7.4 или упражнения 7.5,
в которой каждый пункт следующего списка встречается хотя бы один раз:
• Завершение цикла по проверке условия в команде while.
• Управление продолжительностью выполнения цикла в зависимости от переменной
active.
• Выход из цикла по команде break, если пользователь вводит значение 'quit'."""

# question_1 = "Write your name here: "
#
# while True:
#     message = input(question_1)
#     if message == "quit":
#         break
#     else:
#         print(message)
#
# x = 1
# while x <= 10:
#     print(x)
#     x += 1


prompt = "\nНапиши что-то и я выведу тебе то что ты написал(черная магия)."
prompt += "\nДля выхода просто напиши 'quit' в консоль.\n"
active = True
while active:
    messages = input(prompt)

    if messages != "quit":
        print(messages)
    else:
        active = False

