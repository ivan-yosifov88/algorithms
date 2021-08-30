def generate_field(size):
    matrix = []
    for row in range(size):
        matrix.append([-1] * size)
    return matrix


def print_result(field):
    for row in field:
        print(row)
    print()


def is_valid_move(field, size, row, col):
    return 0 <= row < size and 0 <= col < size and field[row][col] == -1


def move_knight(field, size, directions, row, col, tracker):
    if tracker == size * size:
        print(move_knight.recursion_count)
        return True

    for row_index, col_index in directions:
        row_new = row + row_index
        col_new = col + col_index

        if is_valid_move(field, size, row_new, col_new):
            field[row_new][col_new] = tracker
            if move_knight(field, size, directions, row_new, col_new, tracker + 1):
                move_knight.recursion_count += 1
                return True
            field[row_new][col_new] = -1
    return False



field_size = 8

initial_row_index = 0
initial_col_index = 0
initial_tracker_value = 1


field = generate_field(field_size)

field[initial_row_index][initial_col_index] = 0

possible_knight_directions = [
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
]

move_knight.recursion_count = 0
move_knight(field, field_size, possible_knight_directions, initial_row_index,
            initial_col_index, initial_tracker_value)

print_result(field)

# possible_knight_directions = [
#     (2, 1),
#     (1, 2),
#     (-1, 2),
#     (-2, 1),
#     (-2, -1),
#     (-1, -2),
#     (1, -2),
#     (2, -1),
# ]

# possible_knight_directions = [
#     (-2, -1),
#     (-2, 1),
#     (-1, 2),
#     (1, 2),
#     (2, 1),
#     (2, -1),
#     (1, -2),
#     (-1, -2),
# ]