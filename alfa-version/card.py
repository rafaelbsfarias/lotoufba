# Import the 'random' module to generate random numbers
import random

# Define a class called 'Card' to represent a card object
class Card:
    # Constructor method that initializes a card object
    def __init__(self):
        # Generate a list of 15 unique random numbers between 1 and 25 (inclusive)
        self.numbers = random.sample(range(1, 26), 15)

    # Custom string representation for the card object
    def __str__(self):
        # Return a string that displays the numbers on the card
        return f"Card Numbers: {self.numbers}"
    


#card = Card()
#print(f"Card '{card}'.")    