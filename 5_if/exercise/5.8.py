"""5.8. Hello Admin: создайте список из пяти и более имен пользователей, включающий имя
'admin'. Представьте, что вы пишете код, который выводит приветственное сообщение для
каждого пользователя после его входа на сайт. Переберите элементы списка и выведите со-
общение для каждого пользователя:
• Для пользователя с именем 'admin’ выведите особое сообщение — например, «Hello
admin, would you like to see a status report?».
• В остальных случаях выводите универсальное приветствие — например, «Hello
Jaden, thank you for logging in again»."""

usr_names = ["user", "adam", "eva", "aida", "admin"]
if usr_names:
    for usr_n in usr_names:
        if "admin".lower() in usr_n:
            print(f"Hello {usr_n}, would you like to see a status report?")
        else:
            print(f"Hello {usr_n}, thank you for logging in again.")
else:
    print("We need to ind some users!")
