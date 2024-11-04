SIDE_LENGTH = 5

call_numbers = map(int, input().split(','))
input()

boards = []
current_board = []
while True:
    try:
        line = input()
    except EOFError:
        boards.append(current_board)
        break

    if not line:
        boards.append(current_board)
        current_board = []
        continue

    row = [ int(piece) for piece in line.split(' ') if piece ]
    current_board.append(row)

pulled_numbers = set()

def board_has_won(board):
    for row in board:
        if all(cell in pulled_numbers for cell in row):
            return True

    for column_id in range(SIDE_LENGTH):
        if all(
            board[row_id][column_id] in pulled_numbers
            for row_id in range(SIDE_LENGTH)
        ):
            return True

    return False

done = False
for call_number in call_numbers:
    pulled_numbers.add(call_number)

    for board in boards:
        if board_has_won(board):
            done = True
            break

    if done:
        break

print(call_number *
    sum(
        cell
        for row in board
        for cell in row
        if cell not in pulled_numbers
    )
)
