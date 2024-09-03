operations = []
while True:
    try:
        line = input()
    except EOFError:
        break

    first_word, second_word, *pieces = line.split(' ')
    pieces = ' '.join(pieces)
    if first_word == 'swap':
        if second_word == 'position':
            indices = tuple(map(int, pieces.split(' with position ')))
            operations.append(('swap position', *indices))
        else: # swap letter
            letters = pieces.split(' with letter ')
            operations.append(('swap letter', *letters))
    elif first_word == 'rotate':
        if second_word == 'based':
            letter = pieces.split(' ')[-1]
            operations.append(('rotate letter', letter))
        else: # rotate left/right
            steps = int(pieces.split(' ')[-2])
            operations.append(('rotate', second_word, steps))
    elif first_word == 'reverse':
        indices = tuple(map(int, pieces.split(' through ')))
        operations.append((first_word, *indices))
    elif first_word == 'move':
        indices = tuple(map(int, pieces.split(' to position ')))
        operations.append((first_word, *indices))

def apply_operation(operation):
    operation_type, *operation_args = operation

    if operation_type == 'swap position':
        lower_index, higher_index = sorted(operation_args)
        lower_letter = password[lower_index]
        higher_letter = password[higher_index]

        return password[:lower_index] + higher_letter + \
            password[lower_index + 1 : higher_index] + lower_letter + \
            password[higher_index + 1:]
    elif operation_type == 'swap letter':
        first_letter, second_letter = operation_args

        return \
            apply_operation(('swap position', \
            password.index(first_letter), \
            password.index(second_letter)))
    elif operation_type == 'rotate letter':
        [letter] = operation_args
        steps = password.index(letter)
        if steps >= 4:
            steps += 1
        steps += 1

        return apply_operation(('rotate', 'right', steps))
    elif operation_type == 'rotate':
        direction, steps = operation_args
        offset = steps * (1 if direction == 'left' else -1)
        password_length = len(password)

        return ''.join([
            password[ (i + offset) % password_length ] for i in range(password_length)
        ])
    elif operation_type == 'reverse':
        lower_index, higher_index = sorted(operation_args)
        reversed_area = password[lower_index : higher_index + 1][::-1]

        return \
            password[:lower_index] + \
            reversed_area + \
            password[higher_index + 1:]
    elif operation_type == 'move':
        source_index, destination_index = operation_args
        source_letter = password[source_index]
        password_without_source_letter = password.replace(source_letter, '')

        return \
            password_without_source_letter[:destination_index] + \
            source_letter + \
            password_without_source_letter[destination_index:]

password = 'abcdefgh'
for operation in operations:
    password = apply_operation(operation)

print(password)
