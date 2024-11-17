workflows = {}
line = input()
while line:
    workflow_name, workflow = line.split('{')
    *rules, catchall_rule = workflow[:-1].split(',')
    workflow = tuple(
        tuple(rule.split(':'))
        for rule in rules
    ) + (catchall_rule, )

    workflows[workflow_name] = workflow
    line = input()

parts = []
while True:
    try:
        line = input()
    except EOFError:
        break

    part_ratings = dict(
        zip(
            'xmas',
            (
                int(parameter.split('=')[1])
                for parameter in line[1:-1].split(',')
            )
        )
    )
    parts.append(part_ratings)

accepted = []
for part in parts:
    workflow = 'in'
    while workflow not in ('A', 'R'):
        *rules, catchall_rule = workflows[workflow]
        found_rule = False
        for rule_test, next_workflow in rules:
            if eval(rule_test, part.copy()):
                found_rule = True
                workflow = next_workflow
                break

        if not found_rule:
            workflow = catchall_rule

    if workflow == 'A':
        accepted.append(part)

print(sum(sum(part.values()) for part in accepted))
