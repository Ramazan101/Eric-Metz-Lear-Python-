"""5.7. Любимый фрукт: составьте список своих любимых фруктов. Напишите серию неза-
висимых команд if для проверки того, присутствуют ли некоторые фрукты в списке.
• Создайте список трех своих любимых фруктов и назовите его favorite_fruits.
• Напишите пять команд if. Каждая команда должна проверять, входит ли опреде-
ленный тип фрукта в список. Если фрукт входит в список, блок if должен выводить
сообщение вида «You really like bananas!»."""

favorite_fruits = ["raspberry", "orange", "mandarin"]
if "raspberry" in favorite_fruits:
    print("You really like raspberry!")
if "orange" in favorite_fruits:
    print("You really like orange!")
if "mandarin" in favorite_fruits:
    print("Your really like mandarin!")
if "banana" in favorite_fruits:
    print("You really like banana!")
if "apple" in favorite_fruits:
    print("You really like apple!")