from heapq import heappush, heappop

SECRET = int(input())
GOAL_X = 31
GOAL_Y = 39

PADDING = 10
MAZE_WIDTH = GOAL_X + PADDING
MAZE_HEIGHT = GOAL_Y + PADDING

generate_tile = lambda x, y: (
    x * (x + 3 + 2*y) + y * (1 + y) + SECRET
).bit_count() % 2 == 0

maze = tuple(
    tuple(
        generate_tile(x, y)
        for x in range(MAZE_WIDTH)
    )
    for y in range(MAZE_HEIGHT)
)

def astar(maze, start, goal):
    # from https://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/

    NEIGHBOR_OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
    close_set = set()
    came_from = {}

    heuristic = lambda a, b: sum(
        (a_coord - b_coord) ** 2 for a_coord, b_coord in zip(a, b)
    )
    gscores = { start : 0 }
    fscores = { start : heuristic(start, goal) }
    oheap = []

    heappush(oheap, (fscores[start], start))

    while oheap:
        _, current = heappop(oheap)
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]

            return data

        close_set.add(current)
        for x_offset, y_offset in NEIGHBOR_OFFSETS:
            x, y = current
            neighbor_x = x + x_offset
            neighbor_y = y + y_offset
            if (
                neighbor_x not in range(MAZE_WIDTH)
                or neighbor_y not in range(MAZE_HEIGHT)
                or not maze[neighbor_y][neighbor_x]
            ):
                continue

            neighbor = (neighbor_x, neighbor_y)
            tentative_g_score = gscores[current] + heuristic(current, neighbor)
            if (
                tentative_g_score < gscores.get(neighbor, 0)
                or (
                    neighbor not in close_set
                    and neighbor not in ( cell for _, cell in oheap )
                )
            ):
                came_from[neighbor] = current
                gscores[neighbor] = tentative_g_score
                fscores[neighbor] = (
                    tentative_g_score + heuristic(neighbor, goal)
                )
                heappush(oheap, (fscores[neighbor], neighbor))

    return False

print(
    len(
        astar(maze, (1, 1), (GOAL_X, GOAL_Y))
    )
)
