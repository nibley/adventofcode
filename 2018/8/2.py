def parse_license():
    global cursor

    num_children = numbers[cursor]
    cursor += 1

    num_metadata = numbers[cursor]
    cursor += 1

    children = []
    for _ in range(num_children):
        children.append(parse_license())

    metadata = []
    for _ in range(num_metadata):
        metadata.append(numbers[cursor])
        cursor += 1

    return (children, metadata)

def node_score(node):
    children, metadata = node

    if not children:
        return sum(metadata)

    score = 0
    num_children = len(children)
    for child_index in metadata:
        if child_index < num_children + 1:
            child_index -= 1
            score += node_score(children[child_index])

    return score

numbers = list(map(int, input().split(' ')))

cursor = 0
root = parse_license()

print(node_score(root))
