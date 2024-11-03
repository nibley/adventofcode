field_ranges = {}
line = input()
while line:
    field_name, right_side = line.split(': ')
    field_ranges[field_name] = tuple(
        tuple( int(n) for n in range_option.split('-') )
        for range_option in right_side.split(' or ')
    )
    line = input()

input()
my_ticket = tuple( int(n) for n in input().split(',') )

input()
input()
tickets = []
while True:
    try:
        line = input()
    except EOFError:
        break

    tickets.append(tuple( int(n) for n in line.split(',') ))

def value_is_valid(value):
    return any(
        any( start <= value <= end for start, end in ranges )
        for ranges in field_ranges.values()
    )

print(
    sum(
        sum(
            value
            for value in ticket
            if not value_is_valid(value)
        )
        for ticket in tickets
    )
)
