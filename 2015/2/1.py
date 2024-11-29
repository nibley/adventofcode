def paper_for_box(box):
    width, height, length = box

    return (
        3 * width * height
        + 2 * (
            width * length
            + height * length
        )
    )

total_paper = 0
while True:
    try:
      line = input()
    except EOFError:
        break

    box = sorted( int(n) for n in line.split('x') )
    total_paper += paper_for_box(box)

print(total_paper)
