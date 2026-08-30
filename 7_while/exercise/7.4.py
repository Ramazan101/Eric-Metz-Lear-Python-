"""7.4. Топпинг для пиццы: напишите цикл, который предлагает пользователю вводить до-
полнения для пиццы до тех пор, пока не будет введено значение 'quit'. При вводе каждого
дополнения выведите сообщение о том, что это дополнение включено в заказ."""

prompt = "Write your toppings for pizza here: "
is_active = True
while is_active:
    message = input(prompt)
    if message == "quit":
        is_active = False
    else:
        print(f"Дополнение включен в заказ: {message}")