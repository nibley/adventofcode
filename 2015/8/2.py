from json import dumps

total_encoded = 0
total_code = 0

r"""
escape types

\\
\"
\x{n}{n}
"""

while True:
    try:
      line = input()
    except EOFError:
        break

    total_encoded += len(dumps(line))
    total_code += len(line)

print(total_encoded - total_code)
