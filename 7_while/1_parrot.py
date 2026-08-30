# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

is_active = True
while is_active:
    message = input(prompt)
    if message == "quit":
        is_active = False
    else:
        print(message)


# messages = ""
# while messages != "quit":
#     messages = input(prompt)
#
#     if messages != "quit":
#         print(messages)
