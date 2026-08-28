# Saving information about order pizza.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# Description order.
print(f"You ordered a {pizza["crust"]}-crust pizza "
      "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)

