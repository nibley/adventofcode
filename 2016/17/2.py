from functools import cache
from hashlib import md5

get_doors = cache(
    lambda path: tuple(
        char in 'bcdef' # True for open, False for closed
        for char in md5(f'{SECRET}{path}'.encode()).hexdigest()[ : 4 ]
    )
)

SECRET = input()
START_POSITION = (0, 0)
GOAL_POSITION = (3, 3)
SIDE_LENGTH = 4
DIRECTIONS = dict(
    zip(
        ('U', 'D', 'L', 'R'),
        ((0, -1), (0, 1), (-1, 0), (1, 0))
    )
)

paths_to_goal = []
paths_to_scan = [('', START_POSITION)]
while paths_to_scan:
    new_paths_found = []

    for path, (x, y) in paths_to_scan:
        for direction, (x_offset, y_offset) in DIRECTIONS.items():
            neighbor_x = x + x_offset
            neighbor_y = y + y_offset

            if (
                neighbor_x in range(SIDE_LENGTH)
                and neighbor_y in range(SIDE_LENGTH)
                and get_doors(path)[ 'UDLR'.index(direction) ]
            ):
                neighbor_path = path + direction
                neighbor_position = (neighbor_x, neighbor_y)

                if neighbor_position == GOAL_POSITION:
                    paths_to_goal.append(neighbor_path)
                else:
                    new_paths_found.append(
                        (neighbor_path, neighbor_position)
                    )

    paths_to_scan = new_paths_found

print(max(map(len, paths_to_goal)))
