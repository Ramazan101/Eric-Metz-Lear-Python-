pets = ["dog", "cat", "dog", "cat", "goldfish", "cat", "rabbit", "cat"]
print(pets)

for pet in pets:
    if "cat" in pet:
        pets.remove("cat")
print(pets)

while "cat" in pets:
    pets.remove("cat")
print(pets)