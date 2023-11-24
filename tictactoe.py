"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total = 0
    for row in board:
        for element in row:
            if (element == X) or (element == O):
                total += 1

    if total % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                actions.add((row, col))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = deepcopy(board)
    if board[i][j] == EMPTY:
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("Cell is not empty")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    c = []
    d = []
    d2 = []
    lines = []
    for i in range(len(board[0])):
        # cols
        c = []
        for x in range(len(board[0])):
            c.append(board[x][i])
        lines.append(c)
        # rows
        lines.append(board[i])
        # diag-left-right
        d.append(board[i][i])
        # diag-right-left
        d2.append(board[i][len(board) - i - 1])
    lines.append(d)
    lines.append(d2)
    #Return winner of game if there is one
    for line in lines:
        if line.count(line[0]) == len(line):
            return line[0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for row in board:
            for cell in row:
                if cell == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax_value(state, alpha, beta):
    """
    Returns utility value if an optimal action is played for the current player on the board.
    """
    if terminal(state):
        return utility(state)
    if player(state) == X:
        func = max
        v = - math.inf
    else:
        func = min
        v = math.inf
    for action in actions(state):
        v = func(v, minimax_value(result(state, action), alpha, beta))
        if player(state) == X:
            alpha = func(alpha, v)
        else:
            beta = func(beta, v)
        if beta <= alpha:
            break
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    for action in actions(board):
        alpha = - math.inf
        beta = math.inf
        if minimax_value(board, alpha, beta) == minimax_value(result(board, action), alpha, beta):
            return action
