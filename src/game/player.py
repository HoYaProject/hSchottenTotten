class Player:
    def __init__(self, drawn_cards):
        self.hand = drawn_cards

    def get_hand(self):
        return self.hand

    def send_card(self, index: int):
        return self.hand.pop(index)

    def add_card(self, card: str):
        self.hand.append(card)