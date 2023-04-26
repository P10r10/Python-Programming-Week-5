def print_sudoku(lst: list):
    for row in range(0, 9):
        for col in range(0, 9):
            if col == 3 or col == 6:  # separates grids horizontally
                print(" ", end="")
            print(f"{'_' if lst[row][col] == 0 else lst[row][col]}", end="")
            if col != 8:  # prevents space at the end of line
                print(" ", end="")
        print()
        if row == 2 or row == 5:  # separates grids vertically
            print()


def copy_and_add(lst: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for row in lst:
        sudoku_copy.append(row.copy())
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy


if __name__ == "__main__":
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
