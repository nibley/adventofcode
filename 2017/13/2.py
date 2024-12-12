from collections import defaultdict

layers = defaultdict(lambda: 0)
while True:
    try:
        line = input()
    except EOFError:
        break

    layer_depth, layer_range = map(int, line.split(': '))
    layers[layer_depth] = layer_range

def scanner_catches(t, delay):
    depth = t - delay
    return layers[depth] and not t % (layers[depth] * 2 - 2)

deepest_depth = max(layers)
delay = 1
while any(
    scanner_catches(t, delay)
    for t in range(delay, delay + deepest_depth + 1)
):
    delay += 1

print(delay)
