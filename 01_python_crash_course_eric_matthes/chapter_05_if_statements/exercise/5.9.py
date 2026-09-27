"""5.9. Без пользователей: добавьте в hello_admin.py команду if, которая проверит, что список
пользователей не пуст.
• Если список пуст, выведите сообщение «We need to ind some users!».
• Удалите из списка все имена пользователей и убедитесь в том, что программа выво-
дит правильное сообщение."""

usr_names = []
if usr_names:
    for usr_n in usr_names:
        if "admin".lower() in usr_n:
            print(f"Hello {usr_n}, would you like to see a status report?")
        else:
            print(f"Hello {usr_n}, thank you for logging in again.")
else:
    print("We need to ind some users!")
