import random
from .define import *


class Card:
    def __init__(self):
        self.card = [
            TRIBE_A1,
            TRIBE_A2,
            TRIBE_A3,
            TRIBE_A4,
            TRIBE_A5,
            TRIBE_A6,
            TRIBE_A7,
            TRIBE_A8,
            TRIBE_A9,
            TRIBE_B1,
            TRIBE_B2,
            TRIBE_B3,
            TRIBE_B4,
            TRIBE_B5,
            TRIBE_B6,
            TRIBE_B7,
            TRIBE_B8,
            TRIBE_B9,
            TRIBE_C1,
            TRIBE_C2,
            TRIBE_C3,
            TRIBE_C4,
            TRIBE_C5,
            TRIBE_C6,
            TRIBE_C7,
            TRIBE_C8,
            TRIBE_C9,
            TRIBE_D1,
            TRIBE_D2,
            TRIBE_D3,
            TRIBE_D4,
            TRIBE_D5,
            TRIBE_D6,
            TRIBE_D7,
            TRIBE_D8,
            TRIBE_D9,
            TRIBE_E1,
            TRIBE_E2,
            TRIBE_E3,
            TRIBE_E4,
            TRIBE_E5,
            TRIBE_E6,
            TRIBE_E7,
            TRIBE_E8,
            TRIBE_E9,
            TRIBE_F1,
            TRIBE_F2,
            TRIBE_F3,
            TRIBE_F4,
            TRIBE_F5,
            TRIBE_F6,
            TRIBE_F7,
            TRIBE_F8,
            TRIBE_F9,
        ]
        random.shuffle(self.card)

    def get_initial_card(self):
        cards = []
        for _ in range(INITIAL_CARD_COUNT):
            cards.append(self.draw_card())
        return cards

    def draw_card(self):
        return self.card.pop()