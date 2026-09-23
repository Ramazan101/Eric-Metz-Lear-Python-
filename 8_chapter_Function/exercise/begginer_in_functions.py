# Задача 1
# Создай функцию square(number), которая возвращает квадрат числа.

def square(number):
    # square_n = number ** 2
    return number ** 2
print(square(2))


# Задача 2
# Создай функцию is_even(number), которая возвращает True,
# если число чётное, и False, если нечётное.


def is_oven(number):
    if number % 2 == 0:
        return "True"
    else:
        return "False"
print(is_oven(2))
# Задача 3
# Создай функцию max_number(a, b), которая возвращает большее число.

def max_number(a, b):
    return max(a, b)
print(max_number(1, 3))
# Задача 4
# Создай функцию get_full_name(first_name, last_name).

def get_full_name(first_name=str, last_name=str, middle_name=None):
    if middle_name:
        return first_name, last_name, middle_name
    return first_name, last_name
n = list(get_full_name("Ramazan", "Ryskulov",))
print(n)
# Задача 5
# Создай функцию calculate_discount(price, discount),
# которая возвращает цену после скидки.

def calculate_discount(price=int, discount=int):
    pass

# Задача 6
# Создай функцию check_password(password).
# Если длина пароля >= 8, вернуть "Надёжный",
# иначе "Слабый".
def check_password(password=str):
    if len(password) > 8:
        return "Your password is confident!"
    else:
        return "Your password is not confident!"
print(check_password("adminadmin"))
# Задача 7
# Создай функцию student_info(name, age, city="Bishkek"),
# которая возвращает словарь:
# {"name": ..., "age": ..., "city": ...}

def student_info(name, age, city) -> None:
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    return person
build_person = student_info("Кракен", 12, "Бишкек")
print(build_person)
