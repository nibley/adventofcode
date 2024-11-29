def unlabeled_balls_in_labeled_boxes(balls, box_sizes):
    # from https://phillipmfeldman.org/Python/combinatorics.html

    # scoops are allocated among ingredients like balls among boxes
    # in classic combinatorics terminology

    if not balls:
        yield (0, )* len(box_sizes)
    elif len(box_sizes) == 1 and box_sizes[0] >= balls:
        yield (balls, )
    else:
        for balls_in_first_box in range(min(balls, box_sizes[0]), -1, -1):
            balls_in_other_boxes = balls - balls_in_first_box
            for distribution_other in unlabeled_balls_in_labeled_boxes(
                balls_in_other_boxes,
                box_sizes[ 1 : ]
            ):
                yield (balls_in_first_box, ) + distribution_other

def recipe_score(recipe):
    recipe_calories = sum(
        ingredient_calories * scoops
        for ingredient_calories, scoops in zip(calories, recipe)
    )
    if recipe_calories != 500:
        return 0

    recipe_score = 1
    for stat_index in range(len(ingredients[0])): # number of ingredient stats
        stat_score = sum(
            ingredient[stat_index] * scoops
            for ingredient, scoops in zip(ingredients, recipe)
        )

        if not stat_score > 0:
            return 0

        recipe_score *= stat_score

    return recipe_score

ingredients = []
calories = []
while True:
    try:
        line = input()
    except EOFError:
        break

    ingredient, *stats = line.replace(',', '').split()
    *stats, ingredient_calories = ( int(stat) for stat in stats[ 1 : : 2 ] )

    ingredients.append(stats)
    calories.append(ingredient_calories)

TOTAL_SCOOPS = 100
print(
    max(
        recipe_score(recipe)
        for recipe in unlabeled_balls_in_labeled_boxes(
            TOTAL_SCOOPS,
            (TOTAL_SCOOPS, ) * len(ingredients)
        )
        if 0 not in recipe
    )
)
