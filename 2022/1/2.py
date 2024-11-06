calorie_amounts = []
current_calorie_amount = 0
while True:
    try:
        line = input()
    except EOFError:
        current_calorie_amount = 0
        break

    if line:
        current_calorie_amount += int(line)
    else:
        calorie_amounts.append(current_calorie_amount)
        current_calorie_amount = 0

print(sum( sorted(calorie_amounts)[-3:] ))
