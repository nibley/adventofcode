def visualize():
    display_grid = [row[:] for row in grid]
    for (x, y), cart_char in carts.values():
        display_grid[y][x] = cart_char

    for row in display_grid:
        print(''.join(row))

    print('\n')

def make_turn(cart_char, turn):
    if turn == 1: # straight
        return cart_char
    
    cart_chars = '^>v<'
    current_index = cart_chars.index(cart_char)
    offset = -1 if turn == 0 else 1 # 0 for left, 1 for right
    
    return cart_chars[ (current_index + offset) % 4 ]

def simulate_tick():
    sorted_carts = sorted(carts.items(), \
        key=lambda item: (item[1][0][1], item[1][0][0]))

    for cart_id, [[x, y], cart_char] in sorted_carts:
        if cart_id not in carts:
            continue # removed in a crash already

        if cart_char == '<':
            new_position = (x - 1, y)
            next_cell = grid[y][x - 1]
            if next_cell == '/':
                cart_char = 'v'
            elif next_cell == '\\':
                cart_char = '^'
        elif cart_char == '>':
            new_position = (x + 1, y)
            next_cell = grid[y][x + 1]
            if next_cell == '/':
                cart_char = '^'
            elif next_cell == '\\':
                cart_char = 'v'
        elif cart_char == '^':
            new_position = (x, y - 1)
            next_cell = grid[y - 1][x]
            if next_cell == '/':
                cart_char = '>'
            elif next_cell == '\\':
                cart_char = '<'
        elif cart_char == 'v':
            new_position = (x, y + 1)
            next_cell = grid[y + 1][x]
            if next_cell == '/':
                cart_char = '<'
            elif next_cell == '\\':
                cart_char = '>'
        
        crashing_carts = [
            cart_id \
            for cart_id, cart in carts.items() \
            if cart[0] == new_position ]
        if crashing_carts:
            del carts[cart_id]
            for crashing_cart in crashing_carts:
                del carts[crashing_cart]
            continue

        if next_cell == '+':
            turn = turn_states[cart_id]
            turn_states[cart_id] = (turn + 1) % 3
            
            cart_char = make_turn(cart_char, turn)

        carts[cart_id] = (new_position, cart_char)

cart_id = 0
carts = {}

row_number = 0
grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    row = list(line)
    for column, char in enumerate(row):
        cart_char = None
        if char in '^v':
            cart_char = char
            row[column] = '|'
        elif char in '<>':
            cart_char = char
            row[column] = '-'

        if cart_char:
            carts[cart_id] = ((column, row_number), cart_char)
            cart_id += 1

    grid.append(row)
    row_number += 1

turn_states = { cart_id : 0 for cart_id in carts.keys() }

t = 0
while len(carts) > 1:
    if len(carts) == 2:
        print(carts)

    simulate_tick()

    t += 1
    # print(f't = {t}')
    # visualize()

print(f'(FINAL) t = {t}')
visualize()

print('Final cart is at:')
print(','.join( map(str, list(carts.values())[0][0]) ))
