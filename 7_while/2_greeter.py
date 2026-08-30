prompt = "If you tell us who are you, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello,{name}")

age = input("Please, write your age here: ")
print(int(age) >= 18)
print(age)
print(type(age))
