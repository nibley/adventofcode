from itertools import product as cartesian_product

nodes = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    
    if not line.startswith('/dev'):
        continue
    
    pieces = [piece for piece in line.split(' ') if piece]
    node_name, *info = pieces
    nodes[node_name] = tuple(map(lambda piece: int(piece[:-1]), info))

node_keys = list(nodes.keys())
pairs = cartesian_product(node_keys, repeat=2)

num_viable_pairs = 0
for pair in pairs:
    first_node_name, second_node_name = pair
    if first_node_name == second_node_name:
        continue
    
    # items are (Size, Used, Avail, Use%)
    first_node = nodes[first_node_name]
    second_node = nodes[second_node_name]
    
    first_node_used = first_node[1]
    if first_node_used == 0:
        continue

    if first_node_used > second_node[2]:
        continue
    
    num_viable_pairs += 1
    
print(num_viable_pairs)
