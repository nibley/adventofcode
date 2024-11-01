from collections import defaultdict

adapters = []
while True:
    try:
        line = input()
    except EOFError:
        break

    adapters.append(int(line))

adapters.append(0)
adapters.sort()
deltas_histogram = defaultdict(lambda: 0)

for i, adapter in enumerate(adapters[ : -1 ]):
    next_adapter = adapters[i + 1]
    delta = next_adapter - adapter
    deltas_histogram[delta] += 1

deltas_histogram[3] += 1 # plug into the built-in adapter
print(deltas_histogram[1] * deltas_histogram[3])
