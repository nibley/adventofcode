*_, prompt_row, _, prompt_column = input().split()
prompt_row, prompt_column = (
    int(coord[ : -1 ])
    for coord in (prompt_row, prompt_column)
)

nth_diagonal = prompt_row + prompt_column - 1
last_triangle_number = 1
for n in range(2, nth_diagonal):
    last_triangle_number = n + last_triangle_number

codes_used_through_previous_diagonal = last_triangle_number
nth_code = codes_used_through_previous_diagonal + prompt_column

multiplier = 252533
divisor = 33554393

last_code = 20151125
for _ in range(nth_code - 1):
    last_code = (last_code * multiplier) % divisor

print(last_code)
