def paper_for_box(box):
    width, height, length = box
    basic_ribbon = 2 * (width + height)
    extra_ribbon = width * height * length

    return basic_ribbon + extra_ribbon

total_ribbon = 0
while True:
    try:
      line = input()
    except EOFError:
        break

    dimensions = sorted([int(n) for n in line.split('x')])
    total_ribbon += paper_for_box(dimensions)

print(total_ribbon)
