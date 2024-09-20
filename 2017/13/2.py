from collections import defaultdict

def scanner_catches(t, layer_range):
    return t % (layer_range * 2 - 2) == 0

layers = defaultdict(lambda: 0)
while True:
    try:
        line = input()
    except EOFError:
        break

    layer_depth, layer_range = map(int, line.split(': '))
    layers[layer_depth] = layer_range

deepest_depth = sorted(layers.keys())[-1]
delay = 1
while True:
    caught = False
    for t in range(delay, delay + deepest_depth + 1):
        depth = t - delay
        if depth in layers and scanner_catches(t, layers[depth]):
            caught = True
            break
    
    if not caught:
        break

    delay += 1

print()
print('Appropriate delay:')
print(delay)
