from functools import cache
from hashlib import md5

@cache
def get_doors(path):
    the_string = f'{secret}{path}'
    the_hash = md5(the_string.encode()).hexdigest()[:4]
    return [char in 'bcdef' for char in the_hash]

def check_move(start, move):
    start_path, start_location = start
    move_direction, move_offset = move
    neighbor_location = (
        start_location[0] + move_offset[0],
        start_location[1] + move_offset[1]
    )
    neighbor = (start_path + move_direction, neighbor_location)

    if 0 <= neighbor_location[0] < maze_size:
        if 0 <= neighbor_location[1] < maze_size:
            doors = get_doors(start_path)
            if doors[door_indices[move_direction]]:
                return neighbor

    return None

secret = input()
start_location = (0, 0)
goal_location = (3, 3)
maze_size = 4

known_paths = set([ ('', start_location) ])
neighbor_offsets = list(zip(
    ['D', 'U', 'R', 'L'],
    [(0, 1), (0, -1), (1, 0), (-1, 0)]
))
door_indices = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3,
}

vault_paths = []
paths_to_try = [('', start_location)]
while paths_to_try:
    new_paths_found = []
    for new_path in paths_to_try:
        path, location = new_path
        for neighbor_offset in neighbor_offsets:
            neighbor = check_move(new_path, neighbor_offset)
            if neighbor is not None:
                if neighbor[1] == goal_location:
                    vault_paths.append(neighbor[0])
                else:
                    new_paths_found.append(neighbor)

    paths_to_try = new_paths_found

print(sorted(len(vault_path) for vault_path in vault_paths)[-1])
