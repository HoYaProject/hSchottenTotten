from .define import *


def create_board():
    board = []
    for row in range(ROW):
        if row == BORDER_ROW:
            board_row = [MATCH_DRAW] * COL
        else:
            board_row = [None] * COL
        board.append(board_row)
    return board