from functools import reduce
from math import inf

def _unlabeled_balls_in_labeled_boxes(balls, box_sizes):
    # from https://phillipmfeldman.org/Python/combinatorics.html
    
    if not balls:
        yield len(box_sizes) * (0, )
    elif len(box_sizes) == 1:
        if box_sizes[0] >= balls:
            yield (balls, )
    else:
        for balls_in_first_box in range(min(balls, box_sizes[0]), -1, -1):
            balls_in_other_boxes = balls - balls_in_first_box
            for distribution_other in _unlabeled_balls_in_labeled_boxes(balls_in_other_boxes, box_sizes[1:]):
                yield (balls_in_first_box, ) + distribution_other

def recipe_score(recipe):
    score = 0

    property_scores = []
    for property_index in range(num_properties - 1): # exclude calories 
        property_score = 0
        for ingredient_name, scoops in zip(ingredient_names, recipe):
            ingredient = ingredients[ingredient_name]
            ingredient_score = ingredient[property_index] * scoops
            property_score += ingredient_score
        if property_score <= 0:
                return 0
        property_scores.append(property_score)
    return reduce(lambda x, y: x * y, property_scores, 1)


total_scoops = 100
ingredients = {} # values contain: capacity, durability, flavor, texture, calories

while True:
    try:
        line = input()
    except EOFError:
        break
    
    ingredient, right_side = line.split(': ')
    properties = right_side.split(', ')
    ingredients[ingredient] = tuple(int(piece.split(' ')[1]) for piece in properties)

ingredient_names = sorted(ingredients.keys())
num_properties = len(ingredients[ingredient_names[0]])

best_score = -inf
best_recipe = None
for recipe in _unlabeled_balls_in_labeled_boxes(total_scoops, [total_scoops] * len(ingredient_names)):
    if 0 in recipe:
        continue

    score = recipe_score(recipe)
    if score > best_score:
        best_score = score
        best_recipe = recipe

for ingredient_name, scoops in zip(ingredient_names, best_recipe):
    print(f'{ingredient_name}: {scoops} scoops')
print(best_score)
