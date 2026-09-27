"""7.1. Прокат машин: напишите программу, которая спрашивает у пользователя, какую ма-
шину он бы хотел взять напрокат. Выведите сообщение с введенными данными (например,
«Let me see if I can find you a Subaru”)."""

question = input("what kind of car would you like to rent? ")
print(f"Let me see if I can find you a {question.title()}")