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
def total_orbits(orbiting_object):
    if orbiting_object not in orbits:
        return 0

    orbited = orbits[orbiting_object]
    return 1 + total_orbits(orbited)

orbiting_objects = orbits.keys()
print(
    sum(
        total_orbits(orbiting_object) 
        for orbiting_object in orbiting_objects))
