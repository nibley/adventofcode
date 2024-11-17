def ribbon_for_box(box):
    width, height, length = box
    return 2 * (width + height) + (width * height * length)

total_ribbon = 0
while True:
    try:
      line = input()
    except EOFError:
        break

    box = sorted( int(n) for n in line.split('x') )
    total_ribbon += ribbon_for_box(box)

print(total_ribbon)
