from itertools import count, groupby

raw = input()

files = {}
space_after = {}

disk = []

block_starts = {}
block_lengths = {}

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

    block_starts[file_id] = len(disk)
    block_lengths[file_id] = a

    for i in range(a):
        disk.append(file_id)

    for i in range(space_after[file_id]):
        disk.append(None)

    file_id += 1


total_spacers = sum(space_after.values())
steps = 0

next_free = -1
final_taken = len(disk) - 1

file_id -= 1
while file_id >= 0:
    steps += 1
    # if not steps % 1000: print(steps)
    # if steps > 10: break
    # print()

    # print(
    # ''.join(
    #     '.' if item is None else str(item)
    #     for item in disk
    # )
    # )

    # print('check file', file_id)

    index = 0
    found_space = False
    for key, group in groupby(disk, lambda item: item is None):
        space = sum(1 for _ in group)
        # print(index, '  ', key, space)
        if key and space >= block_lengths[file_id] and index < block_starts[file_id]:
            # print(index, '  ', key, space)
            # print('    move')
            src_start = block_starts[file_id]
            for i, src_i in enumerate(range(block_lengths[file_id])):
                disk[index + i] = file_id
                disk[src_start + src_i] = None

            found_space = True
            index += space
            break

        index += space


    # if total_spacers == len(disk) - next_free:
    #     print('break')
    #     break
    # print(next_free, final_taken)

    # if total_spacers == len(disk) - disk.index(None):
    # if total_spacers == len(disk) - next_free:
    #     print('break')
    #     break

    # if not found_space: continue
    file_id -= 1

# print(
# ''.join(
#     '.' if item is None else str(item)
#     for item in disk
# )
# )

total = 0
for i, item in enumerate(disk):
    if item is None:
        continue

    # print(item)
    total += i * item

print(total)
