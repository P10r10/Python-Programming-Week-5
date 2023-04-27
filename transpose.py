def transpose(lst: list):
    result = []
    for m in range(len(lst[0])):
        row = []
        for n in range(len(lst[0])):
            row.append(lst[n][m])
        result.append(row)
    lst[:] = result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix)
    transpose(matrix)
    print(matrix)
