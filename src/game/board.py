from .define import *


class Board:
    def __init__(self):
        self.board = []
        for row in range(ROW):
            if row == BORDER_ROW:
                board_row = [MATCH_DRAW] * COL
            else:
                board_row = [None] * COL
            self.board.append(board_row)

    def get_board(self):
        return self.board