compounded_fuel = 0
while True:
    try:
        line = input()
    except EOFError:
        break

    mass = int(line)
    fuel = 0
    while mass > 0:
        new_fuel = max(0, mass // 3 - 2)
        fuel += new_fuel
        mass = new_fuel

    compounded_fuel += fuel    

print(compounded_fuel)
