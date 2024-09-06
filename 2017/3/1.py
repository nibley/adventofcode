square = int(input())

last_square_in_spiral_layer = [1]
layer = 1
while True:
    last_in_layer = last_square_in_spiral_layer[layer - 1] + (8 * layer)
    last_square_in_spiral_layer.append(last_in_layer)

    if square <= last_in_layer:
        break
    
    layer += 1

side_length_in_layer = 2 * layer + 1
steps_from_last_in_layer = last_square_in_spiral_layer[layer] - square
steps_from_corner = steps_from_last_in_layer % (side_length_in_layer - 1)
steps_from_mid_side = abs(layer - steps_from_corner)

taxicab_distance = steps_from_mid_side + layer
print(taxicab_distance)
