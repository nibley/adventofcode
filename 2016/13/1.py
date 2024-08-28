import heapq

def generate_tile(x, y):
    formula = x * (x + 3 + 2*y) + y * (1 + y) + secret
    binary_string = '{0:b}'.format(formula)
    bits_odd = len(binary_string.replace('0', '')) % 2
    return '#' if bits_odd else '.'

def astar(array, start, goal):
    # from https://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
    close_set = set()
    came_from = {}

    heuristic = lambda a, b: (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []
    array_shape = (maze_width, maze_height)

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = (current[0] + i, current[1] + j)
            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array_shape[0]:
                if 0 <= neighbor[1] < array_shape[1]:
                    if array[neighbor[1]][neighbor[0]] == '#':
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

secret = int(input())
goal_x = 31
goal_y = 39

padding = 10
maze_width = goal_x + padding
maze_height = goal_y + padding

maze = []
for y in range(maze_height):
    maze.append([generate_tile(x, y) for x in range(maze_width)])

path = astar(maze, (1, 1), (goal_x, goal_y))

for step in path[::-1]:
    print(step)
print()
print(len(path))
