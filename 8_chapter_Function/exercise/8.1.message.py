"""8.1. Сообщение: напишите функцию display_message() для вывода сообщения по теме,
рассматриваемой в этой главе. Вызовите функцию и убедитесь в том, что сообщение выво-
дится правильно."""

def display_message():
    print("8-chapter: Function!")
display_message()

"""8.2. Любимая книга: напишите функцию favorite_book(), которая получает один пара-
метр title. Функция должна выводить сообщение вида «One of my favorite books is Alice in
Wonderland». Вызовите функцию и убедитесь в том, что название книги правильно пере-
дается как аргумент при вызове функции."""

def favorite_book(title: str):
    print(f"One of my favorite book is {title.title()}")
favorite_book("kok jal")