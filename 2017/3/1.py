goal_square = int(input())

# the largest square found in the most recent spiral layer
largest_square_this_layer = 1
spiral_layer = 0
while goal_square > largest_square_this_layer:
    spiral_layer += 1
    largest_square_this_layer += 8 * spiral_layer

layer_side_length = 2 * spiral_layer + 1

goal_to_largest_square = largest_square_this_layer - goal_square
goal_to_nearest_corner = goal_to_largest_square % (layer_side_length - 1)
goal_to_side_midpoint = abs(spiral_layer - goal_to_nearest_corner)

print(goal_to_side_midpoint + spiral_layer)
