message = "One of Python's is its diverse community."
print(message)

""""Апостроф находится в строке, заключенной в двойные кавычки, так что у интерпретатора Python не возникает проблем с правильной интерпретацией следующей
строки: """
#One of Python's strengths is its diverse community.
"""Однако при использовании одиночных кавычек Python не сможет определить, где
должна заканчиваться строка: """
# message = 'One of Python's is its diverse community.'

#   File "C:\Users\user\PythonProject\Lear_Python\first_chapter_variables_and_simple_data_types\4_apostrophe.py", line 9
#     message = 'One of Python's is its diverse community.'
#                                                         ^
# SyntaxError: unterminated string literal (detected at line 9)
#
# Process finished with exit code 1