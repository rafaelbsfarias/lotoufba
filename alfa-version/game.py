class Game:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return f"Number of Cards: {len(self.cards)}"
