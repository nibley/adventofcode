def compare(first_packet, second_packet):
    first_type, second_type = type(first_packet), type(second_packet)

    if first_type is int and second_type is list:
        first_packet = [first_packet]
        first_type = list
    elif first_type is list and second_type is int:
        second_packet = [second_packet]
        second_type = list

    if first_type is int and second_type is int:
        return first_packet < second_packet
    elif first_type is list and second_type is list:
        if first_packet and not second_packet:
            return False
        elif second_packet and not first_packet:
            return True

        first_head, second_head = first_packet[0], second_packet[0]
        if first_head == second_head:
            return compare(first_packet[1:], second_packet[1:])
        else:
            return compare(first_head, second_head)


packet_pairs = []
while True:
    first_line = input()
    second_line = input()
    packet_pairs.append( (eval(first_line), eval(second_line)) )

    try:
        input()
    except EOFError:
        break

print(
    sum(
        i + 1 if compare(first_packet, second_packet) else 0
        for i, (first_packet, second_packet) in enumerate(packet_pairs)
    )
)
