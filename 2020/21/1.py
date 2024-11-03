ingredients = set()
allergens = set()
foods = []
while True:
    try:
        line = input()
    except EOFError:
        break

    left_side, right_side = line.split(' (contains ')

    food_ingredients = set(left_side.split(' '))
    ingredients.update(food_ingredients)

    food_allergens = set(right_side[:-1].split(', '))
    allergens.update(food_allergens)

    foods.append( (food_ingredients, food_allergens) )

dangerous_ingredients = set.union(
    * (
        set.intersection(
            * (
                food_ingredients
                for food_ingredients, food_allergens in foods
                if allergen in food_allergens
            )
        )
        for allergen in allergens
    )
)

safe_ingredients = ingredients.difference(dangerous_ingredients)
print(
    sum(
        len(food_ingredients.intersection(safe_ingredients))
        for food_ingredients, _ in foods
    )
)
