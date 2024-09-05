# modified from 2015 9

import heapq
from itertools import combinations, permutations
from math import inf

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

'''
def parse_edge(line):
    left_side, cost = line.split(' = ')
    source, destination = left_side.split(' to ')
    edges.setdefault(source, {})
    edges[source][destination] = int(cost)
'''

def get_edge(source, destination):
    if source in edges and destination in edges[source]:
        return edges[source][destination]
    
    return edges[destination][source]
    
def path_cost(path):
    total_cost = get_edge('0', path[0])
    for i, source in enumerate(path[:-1]):
        destination = path[i + 1]
        total_cost += get_edge(source, destination)
    return total_cost

maze = []
waypoints = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    maze_row = []
    for column, char in enumerate(line):
        if char == '#':
            maze_row.append(False)
        else:
            maze_row.append(True)

            if char != '.': # waypoint
                row = len(maze)
                waypoints[char] = (column, row)
    
    maze.append(maze_row)

maze_height = len(maze)
maze_width = len(maze[0])

for waypoint in waypoints:
    print(f'{waypoint}\t{waypoints[waypoint]}')

'''
print()
for maze_row in maze:
    print(''.join(['.' if char else '#' for char in maze_row]))
'''

nodes = sorted(list(waypoints.keys()))
node_pairs = combinations(nodes, 2)
edges = {}
for node_pair in node_pairs:
    node_start, node_end = node_pair
    edges.setdefault(node_start, {})
    edges[node_start][node_end] = \
        len(astar( \
            maze, \
            waypoints[node_start], \
            waypoints[node_end]
        ))

nodes_besides_zero = nodes[1:]
paths = permutations(nodes_besides_zero)
cheapest_path = ()
cheapest_cost = inf
for path in paths:
    cost = path_cost(path)
    if cost < cheapest_cost:
        print(f'Found cheaper path {cost}')
        cheapest_path = path
        cheapest_cost = cost

print()
print(' -> '.join(('0', ) + cheapest_path))
print(cheapest_cost)
