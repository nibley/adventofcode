ingredient_ranges = []

while True:
    line = input()

    if not line:
        break

    ingredient_ranges.append(tuple(map(int, line.split('-'))))

ingredient_ids = []
while True:
    try:
        line = input()
    except EOFError:
        break

    ingredient_ids.append(int(line))

def is_fresh(ingredient_id):
    for start, stop in ingredient_ranges:
        if ingredient_id in range(start, stop + 1):
            return True
    
    return False

print(sum( is_fresh(ingredient_id) for ingredient_id in ingredient_ids ))
