from .game.board import *
from .game.card import *
from .game.player import *
from .cli.draw import *

if __name__ == "__main__":
    print("Hello Schotten Totten")

    board = create_board()
    draw_board(board)

    card = Card()

    players = [None, None]
    players[0] = Player(card.get_initial_card())
    players[1] = Player(card.get_initial_card())
