from ..game.define import *


def draw_board(board):
    for row in range(ROW):
        if row == BORDER_ROW:
            draw_border(board[row])
        else:
            draw_player(board[row])


def draw_border(board_row):
    print("-", end="")
    for col in range(COL):
        if board_row[col] == MATCH_DRAW:
            print("---", end="")
        elif board_row[col] == MATCH_P1:
            print("△△△", end="")
        elif board_row[col] == MATCH_P2:
            print("▽▽▽", end="")
        print("-", end="")
    print()


def draw_player(board_row):
    print(" ", end="")
    for col in range(COL):
        if board_row[col]:
            print(f"{board_row[col]}", end="")
        else:
            print("   ", end="")
        print(" ", end="")
    print()