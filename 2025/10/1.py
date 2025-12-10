from itertools import count, combinations_with_replacement

machines = []

while True:
    try:
        line = input()
    except EOFError:
        break

    goal_lights, *buttons, _ = line.split()

    goal_lights = tuple(
        light == '#'
        for light in goal_lights[ 1 : -1 ]
    )
    
    buttons = tuple(
        tuple(map(int, button[ 1 : -1 ].split(',')))
        for button in buttons
    )

    machines.append( (goal_lights, buttons) )

def get_button_choices(buttons):
    for button_presses in count():
        yield from combinations_with_replacement(buttons, button_presses)

def apply_button_choice(total_lights, button_choice):
    lights = [False] * total_lights

    for button in button_choice:
        for light_index in button:
            lights[light_index] = not lights[light_index]
    
    return tuple(lights)

total = 0
for goal_lights, buttons in machines:
    for button_choice in get_button_choices(buttons):
        resulting_lights = apply_button_choice(len(goal_lights), button_choice)
        if resulting_lights == goal_lights:
            total += len(button_choice)
            break

print(total)
