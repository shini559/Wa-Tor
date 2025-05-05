import random
from typing import List

from src.core.entity.position import Position


class Fish:
    def __init__(self, pos: Position):
        self.age = 0
        self._reproduction_timer: int = 0

        self.position: Position = pos
        self.last_position: Position = pos

        self.voisin: List[Position] = []
        self.move_dispo: List[Position] = []
        self.voisins_entity: List[Fish] = []

        self._alive: bool = True

        self.is_naissance: bool = False

    def move(self) -> None:
        """

        :param pos:
        :return:
        """
        # fish.move_dispo[random.randint(0, len(fish.move_dispo) - 1)]
        pos = self.move_dispo[random.randint(0, len(self.move_dispo) - 1)]

        self.last_position = self.position

        self.position = pos

        self.move_dispo.clear()

    @property
    def last_move(self) -> Position:
        """
        return the last position
        :return: tuple[x,y]
        """
        return self.last_position

    def naissance(self, planet: "Planet"):
        pass

    def is_alive(self) -> bool:
        """

        :return:
        """
        return self._alive

    def get_voisins(self, planet: "Planet"):
        self.voisins = []
        self.voisins_entity = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = self.position.x + dx, self.position.y + dy
            if 0 <= nx < planet.tx and 0 <= ny < planet.ty:
                    if planet.grid[nx][ny] is None:
                        self.move_dispo.append(Position(nx, ny))
                    self.voisins.append((nx, ny))
                    self.voisins_entity.append(planet.grid[nx][ny])



    def set_age(self, age: int):
        pass