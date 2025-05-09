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


    def update(self):
        """
        update the planet
        """
        self.chronon += 1
        moved = set()

        for y in range(HEIGHT):
            for x in range(WIDTH):
                entity = self.grid[y][x]
                if entity is not None and (x, y) not in moved:
                    # Donne à l'entité une référence à la grille
                    entity.set_grid(self.grid)
                    # Laisse l'entité gérer son propre mouvement
                    if entity.move(WIDTH, HEIGHT):
                        moved.add((entity.x, entity.y))
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

    def is_grid_full(self) -> bool:
        """
        Vérifie si toutes les cases sont occupées
        """
        for row in self.grid:
            for cell in row:
                if cell is None:
                    return False
        return True

    def count_fish(self) -> tuple[int, int]:
        """
        Compte le nombre de thons et de requins
        """
        tuna_count = 0
        shark_count = 0
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    if str(cell) == "F":
                        tuna_count += 1
                    elif str(cell) == "S":
                        shark_count += 1
        return tuna_count, shark_count

    def should_stop(self) -> bool:
        """
        Vérifie si la simulation doit s'arrêter
        """
        tuna_count, _ = self.count_entities()
        return self.is_grid_full() or tuna_count == 0