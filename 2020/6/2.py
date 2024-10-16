from functools import cache

orbits = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    orbited, orbiter = line.split(')')
    orbits[orbiter] = orbited

@cache
def path_to_COM(orbiting_object):
    if orbiting_object == 'COM':
        return []

    return path_to_COM(orbits[orbiting_object]) + [orbiting_object]

goal_to_COM = path_to_COM(orbits['SAN'])
me_to_COM = path_to_COM(orbits['YOU'])

common_ancestor = None
for goal_step, me_step in zip(goal_to_COM, me_to_COM):
    if goal_step == me_step:
        common_ancestor = goal_step
    else:
        break

me_to_common_ancestor = me_to_COM[me_to_COM.index(common_ancestor) : ]
common_ancestor_to_goal = goal_to_COM[goal_to_COM.index(common_ancestor) : ]

print(len(me_to_common_ancestor) + len(common_ancestor_to_goal) - 2)
# subtract 1 for double-count of common_ancestor and 1 for my orbit
