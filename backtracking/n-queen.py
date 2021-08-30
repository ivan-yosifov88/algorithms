def create_board(n):
    matrix = []
    for _ in range(n):
        row = [0] * n
        matrix.append(row)

    return matrix


def print_result(board):
    for row in board:
        print(' '.join(str(el) for el in row))


def in_range(board, row, column):
    size = len(board)
    return 0 <= row < size and 0 <= column < size


def is_horizontal_move_valid(board, column, row):
    for c in range(column, -1, -1):
        if board[row][c] == 1:
            return False
    return True


def is_left_upper_diagonal_valid(board, column, row):
    r = row
    for c in range(column, -1, -1):
        if board[r][c] == 1:
            return False

        r -= 1
        if not in_range(board, r, c):
            return True
    return True


def is_lower_left_diagonal_valid(board, column, row):
    r = row
    for c in range(column, -1, -1):
        if board[r][c] == 1:
            return False
        r += 1
        if not in_range(board, r, c):
            return True

    return True


def is_place_valid(board, column, row):
    return is_horizontal_move_valid(board, column, row) and \
           is_left_upper_diagonal_valid(board, column, row) and \
           is_lower_left_diagonal_valid(board, column, row)


def place_the_queen(board, board_size, column):
    if column >= board_size:
        return True

    for row in range(board_size):

        if is_place_valid(board, column, row):
            board[row][column] = 1

            if place_the_queen(board, board_size, column + 1):
                return True
            board[row][column] = 0

    return False


board_size = 4

board = create_board(board_size)

start_column_index = 0


place_the_queen(board, board_size, start_column_index)

print_result(board)
