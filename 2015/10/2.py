current = input()

def look_and_say(sequence):
    groups = []
    current_group = sequence[0]
    for current_number in sequence[1:]:
        if current_number == current_group[-1]:
            current_group += current_number
        else:
            groups.append(current_group)
            current_group = current_number
    groups.append(current_group)

    result = ''
    for group in groups:
        result += f'{len(group)}{group[0]}'
    
    return result


for i in range(50):
    current = look_and_say(current)

print(len(current))
