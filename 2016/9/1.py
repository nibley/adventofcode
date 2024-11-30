import re

compressed = input()
PATTERN = r'\((\d+)x(\d+)\)'

decompressed_length = 0
match = re.search(PATTERN, compressed)
while match is not None:
    length, repetitions = map(int, (match.group(1), match.group(2)))
    start, end = match.start(), match.end()
    decompressed_length += start + repetitions * length

    compressed = compressed[ end + length : ]
    match = re.search(PATTERN, compressed)

decompressed_length += len(compressed)
print(decompressed_length)
