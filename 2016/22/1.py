from itertools import permutations

input()
input()

nodes = []
while True:
    try:
        line = input()
    except EOFError:
        break

    _, _, used, available, _ = ( piece for piece in line.split() if piece )
    assert used[-1] == 'T' and available[-1] == 'T'
    nodes.append( (int(used[ : -1 ]), int(available[ : -1 ])) )

print(
    sum(
        source_used and source_used <= target_available
        for (source_used, _), (_, target_available) in permutations(nodes, 2)
    )
)
