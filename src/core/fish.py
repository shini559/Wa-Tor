import random
from typing import Tuple, List

from src.core.config import WIDTH, HEIGHT


class Fish:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.last_x: int = x
        self.last_y: int = y
        self.age = 0
        self.reproduction_timer: int = 0
        self.__alive: bool = True
        self.grid = None  # Référence à la grille
        self.energy: int = 10  # Initial energy level

    def set_grid(self, grid):
        """
        Définit la référence à la grille
        """
        self.grid = grid

    def get_available_moves(self, width: int, height: int) -> List[Tuple[int, int]]:
        """
        Calcule les mouvements disponibles autour du poisson
        """
        moves = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = (self.x + dx) % width
            new_y = (self.y + dy) % height
            if self.grid[new_y][new_x] is None:
                moves.append((new_x, new_y))
        return moves

    def try_reproduce(self):  # sourcery skip: extract-method
        """
        Essaie de reproduire le poisson

        """
        self.reproduction_timer -= 1
        if self.reproduction_timer <= 0:
            if empty_spaces := self.get_available_moves(WIDTH, HEIGHT):
                baby_x, baby_y = random.choice(empty_spaces)
                baby = self.__class__(baby_x, baby_y)
                baby.set_grid(self.grid)
                self.grid[baby_y][baby_x] = baby

                self.reset_reproduction_timer()
                self.energy -= 5  # Cost of reproduction
                return True
        return False
    
    def reset_reproduction_timer(self):
        """
        Réinitialise le timer de reproduction
        """
        pass

    def move(self, width: int, height: int) -> bool:
        """
        Déplace le poisson sur la grille
        Gére la reproduction
        """
        moves = self.get_available_moves(width, height)
        if not moves:
            self.energy -= 1  # Cost of trying to move
            return False

        self.last_x = self.x
        self.last_y = self.y

        new_x, new_y = random.choice(moves)

        # Met à jour la grille
        self.grid[self.y][self.x] = None
        self.x, self.y = new_x, new_y
        self.grid[new_y][new_x] = self


        # Gère la reproduction
        self.age += 1
        self.try_reproduce()
        return True


    @property
    def last_move(self) -> tuple[int, int]:
        return self.last_x, self.last_y

    def is_alive(self) -> bool:
        return self.__alive
    
