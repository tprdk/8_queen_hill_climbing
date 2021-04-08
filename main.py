import numpy as np
import random

SIZE = 8
MAX_H = 1000

def print_chess_board(board, verbose=True):
    if verbose:
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == -1:
                    print('*', end=' ')
                else:
                    print(board[i][j], end=' ')
            print()
    else:
        for i in range(SIZE):
            for j in range(SIZE):
                if board[i][j] == -1:
                    print('V', end=' ')
                else:
                    print('*', end=' ')
            print()
            

def init_board(board):
    for i in range(SIZE):
        board[random.randint(0, SIZE - 1)][i] = -1
    return board


def wrong_queen(board):
    h = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == -1:
                for row in range(SIZE):
                    if row != i and board[row][j] == -1:
                        h += 1
                for col in range(SIZE):
                    if col != j and board[i][col] == -1:
                        h += 1
                increment = 1
                while increment < SIZE:
                    if i + increment < SIZE and j + increment < SIZE and board[i + increment][j + increment] == -1:
                        h += 1
                    if i - increment >= 0 and j - increment >= 0 and board[i - increment][j - increment] == -1:
                        h += 1
                    if i + increment < SIZE and j - increment >= 0 and board[i + increment][j - increment] == -1:
                        h += 1
                    if i - increment >= 0 and j + increment < SIZE and board[i - increment][j + increment] == -1:
                        h += 1
                    increment += 1
    return h / 2


def calculate_h(board):
    for i in range(SIZE):
        for j in range(SIZE):
            row = 0
            while board[row][j] != -1:
                row += 1
            board[row][j] = 0
            board[i][j] = -1
            board[i][j] = wrong_queen(board)
            board[row][j] = -1
    # print('calculate_h')
    # print_chess_board(board)
    # print('calculate_h\n')
    return board


def find_min_h(board):
    min_h        = MAX_H
    row_index    = []
    column_index = []

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] != -1 and board[i][j] <= min_h:
                if board[i][j] < min_h:
                    row_index.clear()
                    column_index.clear()
                min_h        = board[i][j]
                row_index.append(i)
                column_index.append(j)

    index = random.randint(0, len(row_index) -1)
    # print('find_min_h')
    # print(f'h : {min_h} - row : {row_index[index]} - col : {column_index[index]}')
    # print('find_min_h\n')
    return min_h, row_index[index], column_index[index]


def move_queen(board, row, col):
    for i in range(SIZE):
        if board[i][col] == -1:
            board[i][col]   = 9
            board[row][col] = -1

    # print('move_queen')
    # print_chess_board(board)
    # print('move_queen\n')

    return board

def hill_climbing(board):
    h_min = 2
    iter  = 0
    row   = 0
    col   = 0
    while h_min >= 1:
        h_prev = MAX_H
        board = calculate_h(init_board(board))
        h_min, row, col = find_min_h(board)

        while h_min != 0 and  h_min < h_prev :
            board  = move_queen(board, row, col)
            board  = calculate_h(board)
            h_prev = h_min
            h_min, row, col = find_min_h(board)
        print(f'iter : {iter} prev h : {h_prev} min h : {h_min}')
        iter += 1
    return move_queen(board, row, col)


if __name__ == '__main__':
    chess_board = np.zeros(shape=(SIZE, SIZE), dtype='int')
    chess_board = hill_climbing(chess_board)
    print_chess_board(chess_board, False)