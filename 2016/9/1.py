import re

compressed = input()
pattern = r'\((\d+x\d+)\)'
uncompressed = ''

while True:
    match = re.search(pattern, compressed)
    if match is None:
        break

    length, repetitions = map(int, match.group(1).split('x'))
    start, end = match.start(), match.end()
    uncompressed += compressed[:start]
    uncompressed += compressed[end:end + length] * repetitions
    
    compressed = compressed[end + length:]

uncompressed += compressed
print(len(uncompressed))
