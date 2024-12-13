from itertools import product as cartesian_product

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

        machines.append(
            tuple(
                (int(x), int(y))
                for (_, x), (_, y) in lines
            )
        )

def get_presses(machine):
    (a_x, a_y), (b_x, b_y), (goal_x, goal_y) = machine

    for a_count, b_count in cartesian_product(
        range(1, 100 + 1),
        range(1, 100 + 1)
    ):
        if (
            (a_count * a_x) + (b_count * b_x) == goal_x
            and (a_count * a_y) + (b_count * b_y) == goal_y
        ):
            return 3 * a_count + b_count

    return 0

print(sum(map(get_presses, machines)))
