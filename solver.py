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


def solve():
    pass


def safe(board, pos, num):
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

    # Find which subgrid to check
    subRow = row - row % 3
    subCol = col - col % 3

    # Check if num is in current 3x3 subgrid
    for x in range(3):
        for y in range(3):
            if board[subRow + x][subCol + y] == num:
                return False

    return True


if safe(board, (1, 7), 8) == True:
    print("Safe")
else:
    print("Unsafe")

""" pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(board) """
