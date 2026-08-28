# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "points": 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)


# создание пустого листа для хранения пришельцев.
aliens_numbers = range(1, 31)
aliens = []
# создаем 30 зеленых пришельцев.
for alien_numbers in aliens_numbers:
    new_alien = {"color": "green", "points": 5, "speed": "low"}
    aliens.append(new_alien)


for alien_change in aliens[0:3]:
    if alien_change["color"] == "green":
        alien_change["color"] = "yellow"
        alien_change["speed"] = "medium"
        alien_change["points"] = 10
    elif alien_change["color"] == "yellow":
        alien_change["color"] = "red"
        alien_change["speed"] = "fast"
        alien_change["points"] = 15
    else:
        print("Yr if not correct")

# вывод первых 5 пришельцев.
for alien in aliens[0:10]:
    print(alien)
print("...")

print(f"Total numbers of aliens : {len(aliens)}")
