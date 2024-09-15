def distance_from_origin(steps):
    north_south_position = 0
    northeast_southwest_position = 0
    northwest_southeast_position = 0
    for step in steps:
        if step == 'n':
            north_south_position += 1
        elif step == 's':
            north_south_position -= 1
        elif step == 'ne':
            northeast_southwest_position += 1
        elif step == 'sw':
            northeast_southwest_position -= 1
        elif step == 'nw':
            northwest_southeast_position += 1
        elif step == 'se':
            northwest_southeast_position -= 1

    while True:
        if north_south_position > 0 and northeast_southwest_position < 0:
            north_south_position -= 1
            northeast_southwest_position += 1

            northwest_southeast_position += 1
        elif north_south_position > 0 and northwest_southeast_position < 0:
            north_south_position -= 1
            northwest_southeast_position += 1

            northeast_southwest_position += 1
        elif northeast_southwest_position > 0 and northwest_southeast_position > 0:
            northeast_southwest_position -= 1
            northwest_southeast_position -= 1

            north_south_position += 1
        elif northeast_southwest_position < 0 and northwest_southeast_position < 0:
            northeast_southwest_position += 1
            northwest_southeast_position += 1

            north_south_position -= 1
        elif north_south_position < 0 and northeast_southwest_position > 0:
            north_south_position += 1
            northeast_southwest_position -= 1

            northwest_southeast_position -= 1
        elif north_south_position < 0 and northwest_southeast_position > 0:
            north_south_position += 1
            northwest_southeast_position -= 1

            northeast_southwest_position -= 1
        else:
            break # done reducing final position

    north_south_absolute = abs(north_south_position)
    northeast_southwest_absolute = abs(northeast_southwest_position)
    northwest_southeast_absolute = abs(northwest_southeast_position)

    return \
        north_south_absolute + \
        northeast_southwest_absolute + \
        northwest_southeast_absolute

raw = input()
child_path = raw.split(',')
longest_distance = 0
for i in range(1, len(child_path)):
    distance = distance_from_origin(child_path[ : i])
    if distance > longest_distance:
        longest_distance = distance

print()
print(longest_distance)

# TODO just add some of the three axis scores from first try?
