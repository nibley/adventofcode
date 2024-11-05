from collections import defaultdict

molecule = input()
input()

rules = {}
while True:
    try:
        line = input()
    except EOFError:
        break

    start, end = line.split(' -> ')
    rules[start] = end

def simulate_turn(molecule):
    result = ''
    for i, char in enumerate(molecule[:-1]):
        next_char = molecule[i + 1]
        insertion = rules[char + next_char]

        result += char + insertion
    
    result += molecule[-1]
    return result

for _ in range(10):
    molecule = simulate_turn(molecule)

histogram = defaultdict(lambda: 0)
for char in molecule:
    histogram[char] += 1

frequencies = sorted(histogram.values())
print(frequencies[-1] - frequencies[0])
