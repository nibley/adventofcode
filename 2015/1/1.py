the_input = input()
floor = 0
for c in the_input:
    if c == '(': floor += 1
    elif c == ')': floor -= 1
print(floor)
