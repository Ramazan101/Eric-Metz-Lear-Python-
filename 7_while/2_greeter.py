# prompt = "If you tell us who are you, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"Hello,{name}")
#
# age = input("Please, write your age here: ")
# print(int(age) >= 18)
# print(age)
# print(type(age))

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Бесконечный цикл!
while True:
    print("Please tell me your name:")
    print("enter 'q' at any time quit.")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
