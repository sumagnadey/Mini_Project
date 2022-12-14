"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

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
    num_x, num_o = 0, 0
    for channel in board:
        num_x = num_x + channel.count(X)
        num_o = num_o + channel.count(O)
    
    #including starting case
    if num_x <= num_o:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    num_moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                num_moves.add((i, j))
    return num_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    board_copy = deepcopy(board)
    row, col = action
    if board_copy[row][col] == None:
        board_copy[row][col] = current_player
        return board_copy
    else:
        raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    players = [X, O]
    
    #Generate ColumnList
    colList = [[row[i] for row in board] for i in range(3)]

    #Generate Diagonal List
    diaList = []
    diaList.append([board[i][i] for i in range(len(board))])
    diaList.append([board[i][len(board)-i-1] for i in range(len(board))])

    #check for two players
    for player in players:

        #1. Checking row
        for row in board:
            if row == [player]* 3:
                return player
        
        #2. Checking Column
        for col in colList:
            if col == [player]* 3:
                return player

        #3. Checking Diagonal
        for dia in diaList:
            if dia == [player]* 3:
                return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #If there is a winner
    if winner(board) != None:
        return True
    
    else:
        for row in board:
            if EMPTY in row:
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_game = winner(board)
    if winner_game == X:
        return 1
    elif winner_game == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        return max_val(board)[1]
    else:
        return min_val(board)[1]
    


def max_val(board):
    optimal_action = None
    if terminal(board):
        return (utility(board), optimal_action)
    else:
        start_value = -math.inf
        for action in actions(board):
            minvalue = min_val(result(board, action))[0]
            if minvalue > start_value:
                start_value = minvalue
                optimal_action = action
        return start_value, optimal_action


def min_val(board):
    optimal_action = None
    if terminal(board):
        return (utility(board), optimal_action)
    else:
        start_value = math.inf
        for action in actions(board):
            maxvalue = max_val(result(board, action))[0]
            if maxvalue < start_value:
                start_value = maxvalue
                optimal_action = action
        return start_value, optimal_action