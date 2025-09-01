
from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Initialize the die with a specified number of sides (default is 6)."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random number between 1 and 6."""
        return randint(1, self.num_sides)