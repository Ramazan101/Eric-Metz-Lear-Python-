favorite_languages = {
    "david": "Python",
    "shasha": "C",
    "silvana": "C",
    "cork": "JS",
}
language = favorite_languages["shasha"].title()
print(f"Shasha's favorite language is {language}.")

for key, value in favorite_languages.items():
    print(f"{key.title()}'s favorite language is {value.title()}.")
print("That's all.\n")