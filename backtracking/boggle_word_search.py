def generate_empty_matrix(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def get_matrix_with_chars(is_test=False):
    if is_test:
        return [
            ["T", "Y", "R", "S"],
            ["N", "U", "A", "K"],
            ["Z", "F", "E", "O"],
            ["A", "C", "B", "O"]
        ]


def get_searched_words(is_test=False):
    if is_test:
        return {"RAY", "BOOKS", "AUNT", "FAKE"}


def move_is_valid(row, col, matrix):
    size = len(matrix)
    return 0 <= row < size and 0 <= col < size and matrix[row][col] == 0


def get_chars_that_word_starts_with(searched_words):
    first_chars = ''
    for word in searched_words:
        first_chars += word[0]
    return first_chars


def find_word(row_index, col_index, matrix_with_chars, track_matrix, word, searched_words):
    word = ''.join([word, matrix_with_chars[row_index][col_index]])
    track_matrix[row_index][col_index] = 1

    if word in searched_words:
        print(word)

    for row in range(row_index - 1, row_index + 2):
        for col in range(col_index - 1, col_index + 2):
            if move_is_valid(row, col, track_matrix):
                find_word(row, col, matrix_with_chars, track_matrix, word, searched_words)
    track_matrix[row_index][col_index] = 0




searched_words = get_searched_words(is_test=True)

matrix_with_chars = get_matrix_with_chars(is_test=True)

size = len(matrix_with_chars)

track_matrix = generate_empty_matrix(size)

first_chars_in_searched_words = get_chars_that_word_starts_with(searched_words)

for row_index in range(size):
    for col_index in range(size):
        if matrix_with_chars[row_index][col_index] in first_chars_in_searched_words:
            find_word(row_index, col_index, matrix_with_chars, track_matrix, "", searched_words)