from .game.board import *
from .game.card import *
from .cli.draw import *

if __name__ == "__main__":
    print("Hello Schotten Totten")

    board = create_board()
    draw_board(board)
    card = create_card_dummy()