def paper_for_box(box):
    width, height, length = box
    basic_paper = 2 * (width * height + width * length + height * length)
    extra_paper = width * height

    return basic_paper + extra_paper

total_paper = 0
while True:
    try:
      line = input()
    except EOFError:
        break

    dimensions = sorted([int(n) for n in line.split('x')])
    total_paper += paper_for_box(dimensions)

print(total_paper)
