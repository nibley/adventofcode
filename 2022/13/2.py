from functools import cmp_to_key

def compare(first_packet, second_packet):
    first_type, second_type = type(first_packet), type(second_packet)
    if first_type is int and second_type is int:
        if first_packet == second_packet:
            return 0
        elif first_packet < second_packet:
            return -1
        else:
            return 1
    elif first_type is list and second_type is list:
        if not first_packet and not second_packet:
            return 0
        elif not first_packet:
            return -1
        elif not second_packet:
            return 1

        first_head, second_head = first_packet[0], second_packet[0]
        head_comparison = compare(first_head, second_head)
        if head_comparison == 0:
            return compare(first_packet[1:], second_packet[1:])
        else:
            return head_comparison
    elif first_type is int:
        return compare([first_packet], second_packet)
    elif second_type is int:
        return compare(first_packet, [second_packet])

packets = []
while True:
    first_line = input()
    packets.append(eval(first_line))
    second_line = input()
    packets.append(eval(second_line))

    try:
        input()
    except EOFError:
        break

packets.append([[2]])
packets.append([[6]])

# convert compare from a comparison function to a key function
packets.sort(key=cmp_to_key(compare))

first_divider_index = packets.index([[2]]) + 1
second_divider_index = packets.index([[6]]) + 1
print(first_divider_index * second_divider_index)
