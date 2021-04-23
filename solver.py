import pprint

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def solve(board):
    found = find_empty(board)

    if found:
        row, col = found
    else:
        return True

    for num in range(1, 10):
        if is_safe(board, (row, col), num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    """
    Returns coordinates of empty location on board
    If no empty location found returns null
    :param board: 2d list of ints
    """
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                return (x, y)
    return None


def is_safe(board, pos, num):
    """
    Returns if the attempted move is safe
    :param board: 2d list of ints
    :param pos: (row,col)
    :param num: int
    """
    row = pos[0]
    col = pos[1]
    # Check if num is in current row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if num is in current column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Find which subgrid num is in
    subRow = row - row % 3
    subCol = col - col % 3

    # Check if num is in current 3x3 subgrid
    for x in range(3):
        for y in range(3):
            if board[subRow + x][subCol + y] == num:
                return False

    return True


if solve(board):
    pp = pprint.PrettyPrinter(width=41, compact=True)
    pp.pprint(board)
else:
    print("No solution found!")
