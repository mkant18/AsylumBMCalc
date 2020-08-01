WEIGHTS = {
    "coke": 3,
    "diamond": 4,
    "meth": 2
}

RECIPES = {
    "MK1": {"coke": 13, "diamond": 4, "meth": 0, "money": 0},
    "LIM": {"coke": 0, "diamond": 2, "meth": 8, "money": 3750},
    "MK200": {"coke": 0, "diamond": 2, "meth": 6, "money": 1870}
}


def get_recipe_weight(recipe_name):
    total = 0
    recipe = RECIPES[recipe_name]
    for ingredient in WEIGHTS.keys():
        total += recipe[ingredient] * WEIGHTS[ingredient]
    return total


def get_inventory():
    coke = int(input("Enter how much unprocessed cocaine you have: "))
    diamond = int(input("Enter how much uncut diamond you have: "))
    meth = int(input("Enter how much meth you have: "))
    weight_cap = int(input("How much Y inventory can you fit (weight, add 120 from person): "))
    print(f"You entered:\n{coke} coke\n{diamond} diamond\n{meth} meth")
    return {
        "coke": coke,
        "diamond": diamond,
        "meth": meth,
        "weight_cap": weight_cap
    }


inventory = get_inventory()

print("Please select a recipe: ", end='')
for selected_recipe in RECIPES.keys():
    print(selected_recipe, end='; ')
selected_recipe = input('\n').upper()
while selected_recipe not in RECIPES.keys():
    selected_recipe = input("Bro Ur Kinda Retarted, Try Again: ").upper()
print(f"You've selected {selected_recipe}")
recipe = RECIPES[selected_recipe]

recipe_weight = get_recipe_weight(selected_recipe)

weight_rem = inventory["weight_cap"]


def has_exceeded_inventory(recipe_count):
    for ingredient in WEIGHTS.keys():
        if recipe[ingredient] * recipe_count > inventory[ingredient]:
            return False
    return True


recipe_count = 0
while weight_rem > recipe_weight and not has_exceeded_inventory(recipe_count):
    weight_rem -= recipe_weight
    recipe_count += 1

print(f"You will be making {recipe_count} {selected_recipe}s.")
for ingredient in recipe.keys():
    print(f"You will need {recipe_count * recipe[ingredient]} {ingredient}")

print("Done. Made in PyCharm :) Thonny is a cool editor too.")
