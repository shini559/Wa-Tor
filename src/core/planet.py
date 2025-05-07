import itertools
from src.core.config import WIDTH, HEIGHT
from src.core.fish import Fish
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
            self.grid[y][x] = Tuna(x, y)

        for _ in range(NB_SHARK):
            x, y = positions.pop()
            self.grid[y][x] = Shark(x, y)

    def count_fish(self):
        """Compte le nombre de requins et de thons sur la planète"""

        nb_tuna = 0
        nb_shark = 0

        for row in self.grid:
            for entity in row:
                if isinstance(entity, Tuna):
                    nb_tuna += 1
                elif isinstance(entity, Shark):
                    nb_shark += 1
        return nb_tuna, nb_shark

    def update(self):
        """
        update the planet
        """
        nb_tuna, nb_shark = self.count_fish()

        self.chronon += 1
        moved = set()

        for y, x in itertools.product(range(HEIGHT), range(WIDTH)):  # Correction ici
            entity = self.grid[y][x]
            if entity is not None and (x, y) not in moved:
                # Simule des cases autour disponibles
                entity.move_dispo = [
                    self.toroidal_position(x + dx, y + dy)
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    if self.grid[self.toroidal_position(x + dx, y + dy)[1]][
                           self.toroidal_position(x + dx, y + dy)[0]] is None
                ]

                if entity.move_dispo:
                    entity.move()  # Appel à la méthode move() de l'entité
                    new_x, new_y = entity.x, entity.y
                    self.grid[new_y][new_x] = entity
                    self.grid[y][x] = None
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


