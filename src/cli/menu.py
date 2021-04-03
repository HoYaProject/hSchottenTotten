import random


def player_menu():
    try:
        num_players: int = int(input("Select Number of Players (0 ~ 2): "))
        order: int = 0
        if num_players == 1:
            order = int(input("Select Order (1 or 2): "))
            if order != 1 and order != 2:
                order = random.randint(1, 2)
        elif num_players > 2:
            num_players = 2
    except:
        num_players = 0
        order = 0
    finally:
        return num_players, order
