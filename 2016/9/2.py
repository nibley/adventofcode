import re

compressed = input()
PATTERN = r'\((\d+)x(\d+)\)'

def decompressed_length(compressed):
    match = re.search(PATTERN, compressed)
    if match is None:
        return len(compressed)

    length, repetitions = map(int, (match.group(1), match.group(2)))
    start, end = match.start(), match.end()

    return (
        start
        + decompressed_length(compressed[ end : end + length ]) * repetitions
        + decompressed_length(compressed[ end + length : ])
    )

print(decompressed_length(compressed))
