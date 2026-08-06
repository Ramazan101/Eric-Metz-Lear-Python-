"""3.11. Намеренная ошибка: если ни в одной из предшествующих программ вы еще не сталкивались с ошибками индексирования, попробуйте создать такую ошибку искусственно.
Измените индекс в одной из программ, чтобы вызвать ошибку индексирования. Не забудьте исправить ошибку перед тем, как закрывать программу."""

fruits = ["apple", "cherry", "pineapple"]
print(f"Намеренная ошибка index error: {fruits[-4]}")

# Traceback (most recent call last):
#   File "C:\Users\user\PythonProject\Lear_Python\second_chapter_lists\exercise\index_error.py", line 5, in <module>
#     print(f"Намеренная ошибка index error: {fruits[-4]}")
#                                             ~~~~~~^^^^
# IndexError: list index out of range

