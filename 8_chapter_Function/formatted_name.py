def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("roman", "alochovsky")
print(musician)

"""Необязательные аргументы"""
# first try
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("roman", "burov", "alochovsky")
print(musician)

#current version
def get_formatted_name(first_name, last_name, middle_name = str("")):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi", "hendrix")
print(musician)
print(get_formatted_name("alan", "frerich", "alies"))