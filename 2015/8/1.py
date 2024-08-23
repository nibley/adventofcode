from re import sub
total_code = 0
total_memory = 0

r"""
escape types

\\
\"
\x{n}{n}
"""

def memory_chars(line):
    line = line.replace(r'\\', '_')
    line = line.replace(r'\"', '_')
    line = sub(r'\\x[a-f0-9]{2}', '_', line)
    return len(line) - 2

while True:
    try:
      line = input()
    except EOFError:
        break

    total_code += len(line)
    total_memory += memory_chars(line)

print(total_code - total_memory)
