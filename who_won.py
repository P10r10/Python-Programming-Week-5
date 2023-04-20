def count_matching_elements(my_matrix: list, element: int):
    return sum(row.count(element) for row in my_matrix)


def who_won(game_board: list):
    p1 = count_matching_elements(game_board, 1)
    p2 = count_matching_elements(game_board, 2)
    return 0 if p1 == p2 else 1 if p1 > p2 else 2


if __name__ == "__main__":
    print(who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]]))
