from .game.game import *
from .cli.draw import *
from .cli.menu import *

if __name__ == "__main__":
    print("Hello Schotten Totten")

    num_player, order = player_menu()

    game = Game(num_player, order)
