from collections import defaultdict

get_last_word = lambda line: line.split(' ')[-1][:-1]

state = get_last_word(input())
steps = int(input().split(' ')[-2])
input()

rules = {}
while True:
    try:
        rule_state = get_last_word(input())
        current_rule = []

        for _ in range(2):
            input()

            write_value = int(get_last_word(input()))
            move = 1 if get_last_word(input()) == 'right' else -1
            next_state = get_last_word(input())

            current_rule.append( (write_value, move, next_state) )

        rules[rule_state] = tuple(current_rule)
        input()
    except EOFError:
        break

cursor = 0
tape = defaultdict(lambda: 0)
for _ in range(steps):
    current_cell = tape[cursor]
    write_value, move, next_state = rules[state][current_cell]

    tape[cursor] = write_value
    cursor += move
    state = next_state

print(sum(tape.values()))
