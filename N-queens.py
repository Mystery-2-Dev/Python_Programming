#Problem statement 1
import copy
backtrack=0


def get_board(size):

    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def print_solutions(solutions, size):

    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):

    for iy in range(col):
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0:
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0:
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True


def solve(board, col, size):
    global backtrack
    if col >= size:
        return

    for i in range(size):
        if is_safe(board, i, col, size):
            board[i][col] = 1
            if col == size - 1:
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            backtrack+=1
            board[i][col] = 0


def add_solution(board):
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)



size = int(input('What is the size of the chessboard? n = \n'))

board = get_board(size)
solutions = []
solve(board, 0, size)
print_solutions(solutions, size)
print("Total solutions :",len(solutions))

print('Backtracks are:',backtrack)