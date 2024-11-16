def hash_algorithm(string):
    result = 0

    for char in string:
        result += ord(char)
        result *= 17
        result %= 256

    return result

boxes = [ [] for _ in range(256) ]

for step in input().split(','):
    operation_is_lens_add = '=' in step

    if operation_is_lens_add:
        step_label, step_value = step.split('=')
        step_value = int(step_value)
        new_lens = (step_label, step_value)
    else:
        step_label, *_ = step.split('-')

    box_number = hash_algorithm(step_label)
    box = boxes[box_number]

    try:
        label_index = next(
            i
            for i, (lens_label, lens_value) in enumerate(box)
            if lens_label == step_label
        )

        if operation_is_lens_add:
            box[label_index] = new_lens
        else:
            del box[label_index]
    except StopIteration:
        if operation_is_lens_add:
            box.append(new_lens)
        # (if operation is -, do nothing)

print(
    sum(
        (box_number + 1) * (lens_index + 1) * lens_value
        for box_number, box in enumerate(boxes)
        if box
        for lens_index, (_, lens_value) in enumerate(box)
    )
)
