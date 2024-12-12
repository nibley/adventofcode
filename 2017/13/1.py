from collections import defaultdict

def scanner_position(t):
    layer_range = layers[t]
    cycle_length = max(1, layer_range * 2 - 2)

    position = t % cycle_length
    if position > layer_range - 1:
        position = layer_range - (position % (layer_range - 1)) - 1

    return position

layers = defaultdict(lambda: 0)
while True:
    try:
        line = input()
    except EOFError:
        break

    layer_depth, layer_range = map(int, line.split(': '))
    layers[layer_depth] = layer_range

def visualize(t):
    caught = False
    print(f' t = {t}')
    longest_range = sorted(layers.values())[-1]
    print(f' {'   '.join(str(i) for i in range(deepest_depth + 1))}')
    for range_length in range(longest_range):
        for depth in range(deepest_depth + 1):
            layer_range = layers[depth]
            if layer_range > range_length:
                if range_length == scanner_position(t, layer_range):
                    if range_length == 0 and depth == t:
                        cell = '(S)'
                        caught = True
                    else:
                        cell = '[S]'
                else:
                    if range_length == 0 and depth == t:
                        cell = '( )'
                    else:
                        cell = '[ ]'
            else:
                if range_length == 0 and depth == t:
                    cell = '(.)'
                else:
                    cell = '   '
            print(f'{cell} ', end='')
        print()

    if caught:
        print()
        print(f'caught at depth {t}')
    print()

print(
    sum(
        t * layers[t]
        for t in range(max(layers) + 1)
        if scanner_position(t) == 0
    )
)
