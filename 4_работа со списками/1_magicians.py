magicians = ["david", "alice", "roma"]
for magician in magicians:
    print(magician)



for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


for magician in magicians:
    print(f"{magician.capitalize()}, that was a great trick!")
    print(f"I can't to see you next trick, {magician.title()}\n")

print(f"Thank you, everyone. That was great magic show!")


for m in magicians: # тут не было --> :
    print(m)

#   File "C:\Users\user\PythonProject\Lear_Python\4_работа со списками\1_magicians.py", line 18
#     for m in magicians
#                       ^
# SyntaxError: expected ':'
#
# Process finished with exit code 1