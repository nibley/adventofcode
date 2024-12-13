machines = []
while True:
    lines = (input(), input(), input())

    try:
        input()
    except EOFError:
        break
    finally:
        lines = (
            line.replace(',', '').replace('=', '+').split()
            for line in lines
        )

        lines = (
            (x.split('+'), y.split('+'))
            for *_, x, y in lines
        )

        coords = [
            (int(x), int(y))
            for (_, x), (_, y) in lines
        ]

        coords[-1] = tuple(
            goal_coord + 10_000_000_000_000
            for goal_coord in coords[-1]
        )

        machines.append(tuple(coords))

def algebra_solver(machine):
    (a_x, a_y), (b_x, b_y), (goal_x, goal_y) = machine

    # this was once revealed to me on a piece of paper
    count_a = (b_y * goal_x - b_x * goal_y) / (a_x * b_y - a_y * b_x)
    count_b = (a_y * goal_x - a_x * goal_y) / (a_y * b_x - a_x * b_y)

    if count_a.is_integer() and count_b.is_integer():
        return 3 * int(count_a) + int(count_b)
    else:
        return 0

print(sum(map(algebra_solver, machines)))
