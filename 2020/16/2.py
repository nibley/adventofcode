from functools import cache
from math import prod

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

@cache
def value_is_valid(value):
    return any(
        any( start <= value <= end for start, end in ranges )
        for ranges in field_ranges.values()
    )

valid_tickets = tuple(
    ticket
    for ticket in tickets
    if all(value_is_valid(value) for value in ticket)
)

@cache
def position_can_be_field(position, field_name):
    return all(
        any(
            start <= ticket[position] <= end
            for start, end in field_ranges[field_name]
        )
        for ticket in valid_tickets
    )

known_fields = {}
while len(known_fields) < len(my_ticket):
    for position, _ in enumerate(my_ticket):
        possible_fields = tuple(
            field_name
            for field_name in field_ranges
            if (
                field_name not in known_fields
                and position_can_be_field(position, field_name)
            )
        )

        if len(possible_fields) == 1:
            matching_field_name, *_ = possible_fields
            known_fields[matching_field_name] = position

print(
    prod(
        my_ticket[position]
        for field_name, position in known_fields.items()
        if field_name.startswith('departure')
    )
)
