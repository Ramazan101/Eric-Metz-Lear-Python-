"""6.10. Любимые числа: измените программу из упражнения 6.2 (с. 114), чтобы для каждого
человека можно было хранить более одного любимого числа. Выведите имя каждого чело-
века в списке и его любимые числа."""

# Favorite nums
favorite_nums = {
    "ramazan": [77, 69, 81, 27],
    "dildo": [68, 99, 23, 21],
    "mikro": [76, 90, -1, 0],
    "john": [23, -999, 999.99],
    "jame": [26, 21, 24, 26],
}

for names, nums in favorite_nums.items():
    print(f"Name: {names.title()}.")
    print(f"\tYour favorite nums list: {nums}.")