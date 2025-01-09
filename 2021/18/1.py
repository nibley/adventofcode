from math import floor, ceil

pairs = []
while True:
    try:
        line = input()
    except EOFError:
        break

    pairs.append(eval(line))

def split(pair):
    for i, item in enumerate(pair):
        if type(item) is int:
            if item >= 10:
                half = item / 2
                pair[i] = [floor(half), ceil(half)]
                return True
        else:
            did_split = split(item)
            if did_split:
                return True

    return False

def explode_increment_left(increment_value, parents):
    if not parents:
        return

    # get common ancestor with the in-order neighbor we want
    pivot_parent = None
    while parents:
        *parents, (i, parent) = parents

        if i == 1:
            pivot_parent = parent
            break

    if pivot_parent is None:
        return # nothing to increment
    elif type(pivot_parent[0]) is int:
        pivot_parent[0] += increment_value
        return # goal is immediately under the common ancestor

    # increment rightmost descendant
    pair, _ = pivot_parent
    while type(pair[1]) is not int:
        _, pair = pair

    pair[1] += increment_value

def explode_increment_right(increment_value, parents):
    if not parents:
        return

    # get common ancestor with the in-order neighbor we want
    pivot_parent = None
    while parents:
        *parents, (i, parent) = parents

        if i == 0:
            pivot_parent = parent
            break

    if pivot_parent is None:
        return # nothing to increment
    elif type(pivot_parent[1]) is int:
        pivot_parent[1] += increment_value
        return # goal is immediately under the common ancestor

    # increment leftmost descendant
    _, pair = pivot_parent
    while type(pair[0]) is not int:
        pair, _ = pair

    pair[0] += increment_value

def explode(pair, nest=0, parents=()):
    for i, item in enumerate(pair):
        new_parents = parents + ((i, pair) ,)

        if type(item) is int:
            continue
        elif nest == 3 and all( type(subitem) is int for subitem in item ):
            left_value, right_value = item
            pair[i] = 0

            explode_increment_left(left_value, new_parents)
            explode_increment_right(right_value, new_parents)

            return True
        else:
            did_explode = explode(
                item,
                nest + 1,
                new_parents
            )

            if did_explode:
                return True

    return False

def reduce_pair(pair):
    while explode(pair) or split(pair):
        pass

    return pair

total, *pairs = pairs
for pair in pairs:
    total = reduce_pair([total, pair])

def magnitude(pair):
    if type(pair) is int:
        return pair

    left, right = pair
    return 3 * magnitude(left) + 2 * magnitude(right)

print(magnitude(total))
