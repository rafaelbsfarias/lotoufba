import random

class Card:
    def __init__(self):
        self.numbers = random.sample(range(1, 26), 15)

    def __str__(self):
        return f"Card Numbers: {self.numbers}"
