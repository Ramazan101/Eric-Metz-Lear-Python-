my_foods = ["pizza", "potato",  "beshbarmak", "carrot cake"]

for food in my_foods:
    print(f"My favorite foods are: {food}")

mym_foods = my_foods[:]

for mum_f in mym_foods:
    print(f"My mum favorite foods are: {mum_f}")




print(f"My favorite foods are:\n{my_foods}\n")
print(f"Mums favorite foods are:\n{mym_foods}")




# not worked ("never")

my_foods = ['pizza', 'falafel', 'carrot cake']

friends_food = my_foods


friends_food.append("mushrooms")
print(f"This is favorite food my friends: {friends_food}")

print(f"This is my favorite food: {my_foods}")

"""ПРИМЕЧАНИЕ Если какие-то подробности в этом примере кажутся непонятными, не
огорчайтесь. В двух словах, если при работе с копией списка происходит что-то непредвиденное, убедитесь в том, что список копируется с использованием сегмента, как это
делается в нашем первом примере."""

