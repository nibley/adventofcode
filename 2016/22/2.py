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

    node_name = node_name.replace('/dev/grid/node-', '')
    node_x, node_y = node_name.split('-')
    node_x = int(node_x.replace('x', ''))
    node_y = int(node_y.replace('y', ''))

    nodes[(node_x, node_y)] = tuple(map(lambda piece: int(piece[:-1]), info))

node_keys = list(nodes.keys())
pairs = cartesian_product(node_keys, repeat=2)

viable_pairs = []
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
    
    viable_pairs.append(pair)

print(viable_pairs)
print(len(viable_pairs))
