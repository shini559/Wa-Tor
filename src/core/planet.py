import itertools
from src.core.config import WIDTH, HEIGHT
from src.core.tuna import Tuna
from src.core.shark import Shark
import random


class Planet():
    """
    Planet class to represent a word of wa-Tor.
    """
    def __init__(self):
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.chronon = 1

    def initialize(self, NB_TUNA: int, NB_SHARK: int):
        """
        Initialize the planet with a given number of fish and sharks.

        """
        positions = [(x, y) for x in range(WIDTH) for y in range(HEIGHT)]
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]
        random.shuffle(positions)



        for _ in range(NB_TUNA):
            x, y = positions.pop()
            self.grid[x][y] = Tuna(x, y)

        for _ in range(NB_SHARK):
            x, y = positions.pop()
            self.grid[x][y] = Shark(x, y)


    def update(self):
        """
        update the planet
        """
        self.chronon += 1

        # A supprimer plus tard

        moved = set()

        for x, y in itertools.product(range(WIDTH), range(HEIGHT)):
            entity = self.grid[x][y]
            if entity is not None and (x, y) not in moved:
                dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                new_x, new_y = self.toroidal_position(x + dx, y + dy)

                if self.grid[new_x][new_y] is None:
                    self.grid[new_x][new_y] = entity
                    self.grid[x][y] = None
                    #entity.move(new_x, new_y)
                    moved.add((new_x, new_y))
                else:
                    moved.add((x, y))

    def toroidal_position(self, x: int, y: int) -> tuple:
        """
        Calculate the toroidal position of a cell in the grid.
        :param x: x coordinate
        :param y: y coordinate
        :return: tuple of (x, y) coordinates
        """
        return x % WIDTH, y % HEIGHT