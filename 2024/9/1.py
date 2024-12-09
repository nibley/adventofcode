from itertools import count, groupby

raw = input()

# raw = '12345'
# raw = '2333133121414131402'

files = {}
space_after = {}

disk = []

file_id = 0
while raw:
    a, *raw = raw
    a = int(a)

    if raw:
        b, *raw = raw
        space_after[file_id] = int(b)
    else:
        space_after[file_id] = 0

    files[file_id] = a
    # print(file_id, a, 'after', space_after[file_id])

    for i in range(a):
        disk.append(file_id)

    for i in range(space_after[file_id]):
        disk.append(None)

    file_id += 1

# print(files)
# print(len(raw))

total_spacers = sum(space_after.values())
steps = 0

next_free = -1
final_taken = len(disk) - 1
while True:
    steps += 1
    if not steps % 1000: print(steps)
    # if steps > 10: break

    # if next_free == final_taken: break

    # print(
    # ''.join(
    #     '.' if item is None else str(item)
    #     for item in disk
    # )
    # )


    next_free = next(
        i
        for i in count()
        if disk[i] is None
    )


    if total_spacers == len(disk) - next_free:
        print('break')
        break
    # print(next_free, final_taken)

    disk[next_free], disk[final_taken] = disk[final_taken], disk[next_free]
    while disk[final_taken] is None:
        final_taken -= 1

    # if total_spacers == len(disk) - disk.index(None):
    # if total_spacers == len(disk) - next_free:
    #     print('break')
    #     break

# print(
# ''.join(
#     '.' if item is None else str(item)
#     for item in disk
# )
# )

total = 0
for i, item in enumerate(disk):
    if item is None:
        break

    # print(item)
    total += i * item

print(total)
