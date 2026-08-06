motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[3])

# Traceback (most recent call last):
#   File "C:\Users\user\PythonProject\Lear_Python\second_chapter_lists\4_list_index.py", line 2, in <module>
#     print(motorcycles[3])
#           ~~~~~~~~~~~^^^
# IndexError: list index out of range


"""Этот синтаксис порождает ошибку только в одном случае — при попытке получить
последний элемент пустого списка:"""

motorcycles = []
print(motorcycles[-1])

# Traceback (most recent call last):
#  File "motorcyles.py", line 3, in <module>
#  print(motorcycles[-1])
# IndexError: list index out of range


