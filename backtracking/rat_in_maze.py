def get_matrix(is_test=False):
    if is_test:
        matrix = [
    [1, 1, 0, 0],
    [1, 1, 1, 1], 
    [0, 1, 0, 0], 
    [0, 1, 1, 1],
    ]
    # matrix = [
    # [1, 1, 0, 0, 0],
    # [1, 1, 1, 1, 1], 
    # [0, 1, 1, 0, 0], 
    # [0, 0, 1, 1, 1],
    # ]

        return matrix
    
def create_solution_matrix(row_count, col_count):
    solution_matrix = []
    for _ in range(row_count):
        row = [c * 0 for c in range(col_count)]
        solution_matrix.append(row)
    return solution_matrix

def position_in_range(row, col, matrix):
    max_rows = len(matrix)
    max_columns = len(matrix[0])
    return 0 <= row < max_rows and 0 <= col < max_columns

def is_valid_position(row, col, matrix):
    return position_in_range(row, col, matrix) and matrix[row][col] == 1

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(r) for r in row))
    print("-" * len(matrix))

def find_solution(row, col, matrix, solution, solution_matrix):
    if (row, col) == solution and matrix[row][col] == 1:
        solution_matrix[row][col] = 1
        return True

    if is_valid_position(row, col, matrix):
        solution_matrix[row][col] = 1
        
        if find_solution(row + 1, col, matrix, solution, solution_matrix):
            return True
        if find_solution(row, col + 1, matrix, solution, solution_matrix):
            return True

        matrix[row][col] = 0
        return False

    return False

matrix = get_matrix(is_test=True)

matrix_row = len(matrix)
matrix_col = len(matrix[0])

solution_matrix = create_solution_matrix(matrix_row, matrix_col)


winning_coordinatres = (matrix_row - 1, matrix_col- 1)

start_row = 0
start_col = 0

find_solution(start_row, start_col, matrix, winning_coordinatres, solution_matrix)

print_matrix(matrix)

print_matrix(solution_matrix)



