# print("Python")
# print("\tPython")

# Python
# 	Python

"""Разрывы строк добавляются с помощью комбинации символов \n
"""
print("Language:\nPython\nC\nJavaScript")

# Language:
# Python
# C
# JavaScript

"""Табуляции и разрывы строк могут сочетаться в тексте. Скажем, последовательность
"\n\t" приказывает Python начать текст с новой строки, в начале которой располагается табуляция. Следующий пример демонстрирует вывод одного сообщения
с разбиением на четыре строки:   """

# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Languages:
# 	Python
# 	C
# 	JavaScript


"""Удаление пропусков"""

favorite_language = " python "
print(favorite_language.strip()) # python
print(favorite_language)         # python_


"""Пропуски также можно удалить у левого края (в начале) строки при помощи метода lstrip(), а метод strip() удаляет пропуски с обоих концов:
"""
# ❶ >>> favorite_language = ' python '
# ❷ >>> favorite_language.rstrip()
#  ' python'
# ❸ >>> favorite_language.lstrip()
#  'python '
# ❹ >>> favorite_language.strip()
#  'python'







