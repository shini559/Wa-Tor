from config import WIDTH, HEIGHT
from tuna import Tuna
from shark import Shark
import random


class Planet():
    """
    Planet class to represent a word of wa-Tor.
    """
    def __init__(self):
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def initialize(self, nb_poisson: int, nb_requin: int):
        """
        Initialize the planet with a given number of fish and sharks.
        :param nb_poisson:
        :param nb_requin:
        :return:
        """
        positions = [(x, y) for x in range(WIDTH) for y in range(HEIGHT)]
        random.shuffle(positions)



        for _ in range(nb_poisson):
            x, y = positions.pop()
            self.grid[x][y] = Tuna((x, y))

        for _ in range(nb_requin):
            x, y = positions.pop()
            self.grid[x][y] = Shark((x, y))

    def display(self):
            """
            Display the current state of the planet grid in the terminal.
            """
            for row in self.grid:
                line = ""
                for cell in row:
                    if cell is None:
                        line += "~ "
                    else:
                        line += str(cell) + " "
                print(line)
            print()



