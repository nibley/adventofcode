seeds = tuple(map(int, input().split(': ')[1].split()))
input()

almanac_maps = []
while True:
    try:
        input()
        map_ranges = []

        map_range = input()
        while map_range:
            destination, source, length = map(int, map_range.split(' '))
            map_ranges.append( (source, source + length, destination) )
            map_range = input()
    except EOFError:
        break
    finally:
        map_ranges.sort()
        almanac_maps.append(map_ranges)

locations = []
for seed in seeds:
    for a_map in almanac_maps:
        for start, stop, offset in a_map:
            if start <= seed < stop:
                seed += offset - start
                break

    locations.append(seed)

print(min(locations))
