prompt = input()
right_side = prompt.split('  ')[1].split('Enter the code at ')[1].split(', ')
prompt_row = int(right_side[0].split(' ')[1])
prompt_column = int(right_side[1].split(' ')[1].replace('.', ''))

nth_diagonal = prompt_row + prompt_column - 1
triangle_numbers = {1: 1}
for n in range(2, nth_diagonal):
    triangle_numbers[n] = n + triangle_numbers[n - 1]

codes_used_through_previous_diagonal = triangle_numbers[nth_diagonal - 1]
nth_code = codes_used_through_previous_diagonal + prompt_column

multiplier = 252533
divisor = 33554393
codes = {1: 20151125}
for n in range(2, nth_code + 1):
    code = (multiplier * codes[n - 1]) % divisor
    codes[n] = code

print(codes[nth_code])
