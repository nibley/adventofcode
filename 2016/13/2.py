from functools import cache

@cache
def generate_tile(x, y):
    formula = x * (x + 3 + 2*y) + y * (1 + y) + secret
    binary_string = '{0:b}'.format(formula)
    bits_odd = len(binary_string.replace('0', '')) % 2
    return '#' if bits_odd else '.'

def check_move(start, move):
    neighbor = (start[0] + move[0], start[1] + move[1])

    if 0 <= neighbor[0] < maze_width:
        if 0 <= neighbor[1] < maze_height:
            if generate_tile(*neighbor) == '.':
                return neighbor

    return False

secret = int(input())
start_location = (1, 1)
num_moves = 50
maze_width = num_moves + start_location[0] + 1
maze_height = num_moves + start_location[1] + 1

locations = set([start_location])
location_neighbors = {}
neighbor_offsets = [(0,1),(0,-1),(1,0),(-1,0)]

for _ in range(num_moves):
    new_locations = []
    for location in locations:
        if location not in location_neighbors:
            valid_neighbors = []
            for neighbor_offset in neighbor_offsets:
                valid_neighbor = check_move(location, neighbor_offset)
                if valid_neighbor:
                    valid_neighbors.append(valid_neighbor)
            location_neighbors[location] = tuple(valid_neighbors)
            new_locations.extend(valid_neighbors)

    if new_locations:
        locations.update(new_locations)

print(len(locations))
