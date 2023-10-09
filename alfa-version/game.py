# Define a class called 'Game' to represent a game object
class Game:
    # Constructor method that initializes a game object
    def __init__(self):
        # Initialize an empty list to store cards in the game
        self.cards = []

    # Method to add a card to the game's list of cards
    def add_card(self, card):
        self.cards.append(card)

    # Custom string representation for the game object
    def __str__(self):
        # Return a string that displays the number of cards in the game
        return f"Number of Cards: {len(self.cards)}"