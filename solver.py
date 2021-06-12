import pprint
import sys

fileName = sys.argv[-1]


def getBoard():
    if len(sys.argv) == 1:
        with open("board.txt") as f:
            board = [list(line.strip()) for line in f]
    else:
        with open(fileName) as f:
            board = [list(line.strip()) for line in f]

    for i in range(len(board)):
        board[i] = list(map(int, board[i]))

    return board


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


def main():
    board = getBoard()
    if solve(board):
        pp = pprint.PrettyPrinter(width=41, compact=True)
        pp.pprint(board)
    else:
        print("No solution found!")


if __name__ == '__main__':
    main()
