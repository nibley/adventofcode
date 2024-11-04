from collections import defaultdict

bit_frequencies = [
    defaultdict(lambda: 0),
    defaultdict(lambda: 0)]
while True:
    try:
        line = input()
    except EOFError:
        break

    for i, char in enumerate(line):
        char = int(char)
        bit_frequencies[char][i] += 1

string_length = len(bit_frequencies[0])
gamma = ''
epsilon = ''
for i in range(string_length):
    zero_frequency = bit_frequencies[0][i]
    one_frequency = bit_frequencies[1][i]

    gamma += '0' if zero_frequency > one_frequency else '1'
    epsilon += '0' if zero_frequency < one_frequency else '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
