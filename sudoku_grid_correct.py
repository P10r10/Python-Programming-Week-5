def row_correct(sudoku: list, row_no: int):
    for i in range(1, 10):  # checks numbers from 1 to 9
        if sudoku[row_no].count(i) > 1:
            return False
    return True


def column_correct(sudoku: list, column_no: int):
    for i in range(1, 10):  # checks numbers from 1 to 9
        if [row[column_no] for row in sudoku].count(i) > 1:
            return False
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    my_block = []  # creates list to accommodate a block
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            my_block.append(sudoku[i][j])
    for i in range(1, 10):  # checks numbers from 1 to 9
        if my_block.count(i) > 1:
            return False
    return True


def sudoku_grid_correct(sudoku: list):
    for row in range(0, 9):  # checks rows 1 to 9 (index 0..8)
        if not row_correct(sudoku, row):
            return False
    for col in range(0, 9):  # checks columns 1 to 9 (index 0..8)
        if not column_correct(sudoku, col):
            return False
    for row in range(0, 8, 3):  # checks 9 sudoku grids
        for col in range(0, 8, 3):
            if not block_correct(sudoku, row, col):
                return False
    return True


if __name__ == "__main__":
    sudoku1 = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
        [2, 6, 7, 8, 3, 9, 5, 0, 4],
        [9, 0, 3, 5, 1, 0, 6, 0, 0],
        [0, 5, 1, 6, 0, 0, 8, 3, 9],
        [5, 1, 9, 0, 4, 6, 3, 2, 8],
        [8, 0, 2, 1, 0, 5, 7, 0, 6],
        [6, 7, 4, 3, 2, 0, 0, 0, 5],
        [0, 0, 0, 4, 5, 7, 2, 6, 3],
        [3, 2, 0, 0, 8, 0, 0, 5, 7],
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
