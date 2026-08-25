# alien_0 = {
#     "color": "green",
#     "points": 4
# }
#
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")
#
#
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)
# print(alien_0["color"])
# print(alien_0["points"])
#
#
# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["points"] = 5
# print(alien_0)
#
# print(f"The alien is {alien_0["color"]}.")
#
# alien_0["color"] = "yellow"
# print(f"\nThe alien is now {alien_0["color"]}")


# alien_0 = {"x_positon": 0, "y_position": 25, "speed": "medium"}
# print(alien_0)
# alien_0["speed"] = "fast"

# Пришелец перемещается вправо
# Вычисляем величину смещения на основании текущей скорости.
# if alien_0["speed"] == "low":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     # пришелец двигается быстро
#     x_increment = 3
#
# alien_0["x_positon"] = alien_0["x_positon"] + x_increment
# print(f"New position: {alien_0["x_positon"]}")
# print(alien_0)

alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["color"]
print(alien_0)


