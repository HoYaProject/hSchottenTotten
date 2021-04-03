from .board import *
from .card import *
from .player import *


class Game:
    def __init__(self, number_of_players: int, order: int = 0):
        self.board = Board()

        self.card = Card()

        player1 = {}
        player2 = {}
        if number_of_players == 0:
            player1["player_type"] = PLAYER_COM
            player2["player_type"] = PLAYER_COM
        elif number_of_players == 1:
            if order == 1:
                player1["player_type"] = PLAYER_USER
                player2["player_type"] = PLAYER_COM
            else:
                player1["player_type"] = PLAYER_COM
                player2["player_type"] = PLAYER_USER
        else:
            player1["player_type"] = PLAYER_USER
            player2["player_type"] = PLAYER_USER
        player1["player_obj"] = Player(self.card.get_initial_card())
        player2["player_obj"] = Player(self.card.get_initial_card())

        self.players = []
        self.players.append(player1)
        self.players.append(player2)
