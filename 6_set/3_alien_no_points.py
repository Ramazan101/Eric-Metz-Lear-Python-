alien_0 = {
    "color": "green",
    "speed": "medium",
    "x_position": 10
}
point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

# This is KeyError: 'points', because in set not have value "points"
# print(alien_0["points"])





